from config.config import config
from config.logging import setup_logger, INFO
from src import kraken_services, trading_services

# Initialize logger
logger = setup_logger(
    __name__,
    config['logging']['trading_engine_filepath'],
    INFO,
)

def trade(last_trade: dict) -> None:
    """
    Implement trading strategy and execute trade.

    Example:
    >>> trade(trading_services.last_trade())
    """

    # If there are no open orders, prepare to create a limit order
    if not kraken_services.open_orders()["result"]["open"]:
        logger.info(f'No open orders detected. Calculating price for new limit order.')

        # Calculate trading fee
        fee = trading_services.trading_fee(
            pair="BTC/USD",
            kraken_ticker=last_trade["pair"],
            ordertype=last_trade["ordertype"],
        )

        # Calculate limit price for new limit order
        limit_price = trading_services.new_limit_price(
            last_trade=last_trade,
            required_return=config["trading"]["required_return"],
            fee=fee,
        )

        logger.info(f'Price for new limit order: {limit_price}')
        # If the last trade was a buy:
        if last_trade["type"] == "buy":
            logger.info(f'Last successful trade was a BUY. Placing a limit SELL order.')

            # Reduce the limit sell volume by a small amount to ensure sufficient crypto balance
            volume = trading_services.reduce_trade_volume(float(last_trade["vol"]))

            # Create a limit sell order
            new_order = kraken_services.add_order(
                ordertype="limit",
                type="sell",
                volume=str(volume),
                pair="BTC/USD",
                price=str(limit_price),
            )

            logger.info(f'Limit SELL order placed for {volume} at {price}.')

        # If the last trade was a sell:
        elif last_trade["type"] == "sell":
            logger.info(f'Last successful trade was a SELL. Placing a limit BUY order.')

            # Calculate maximum purchase volume
            max_buy_vol = trading_services.maximum_buy_volume(
                account_balances=kraken_services.account_balances(),
                price=limit_price,
                precision=5,
            )

            # Create a limit buy order
            new_order = kraken_services.add_order(
                ordertype="limit",
                type="buy",
                volume=max_buy_vol,
                pair="BTC/USD",
                price=str(limit_price),
            )

            logger.info(f'Limit BUY order placed for {max_buy_vol} at {limit_price}.')
