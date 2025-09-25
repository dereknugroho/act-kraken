import src.api_services
import src.services

from src.config import config

def trade(last_trade: dict) -> dict:
    """
    Implement trading strategy and execute trade.

    Example:
    >>> trade(services.last_trade())
    """

    # If there are no open orders, prepare to create a limit order
    if not api_services.open_orders()["result"]["open"]:

        # Calculate trading fee
        trading_fee = services.trading_fee(
            pair="BTC/USD",
            kraken_ticker=last_trade["pair"],
            ordertype=last_trade["ordertype"],
        )

        # Calculate limit price for new limit order
        new_limit_price = services.new_limit_price(
            last_trade=last_trade,
            required_return=config["trading"]["required_return"],
            fee=trading_fee,
        )

        # If the last trade was a buy:
        if last_trade["type"] == "buy":

            # Reduce the limit sell volume by a small amount to ensure sufficient crypto balance
            volume = services.reduce_trade_volume(float(last_trade["vol"]))

            # Create a limit sell order
            new_order = api_services.add_order(
                ordertype="limit",
                type="sell",
                volume=str(volume),
                pair="BTC/USD",
                price=str(new_limit_price),
            )

        # If the last trade was a sell:
        elif last_trade["type"] == "sell":

            # Calculate maximum purchase volume
            max_buy_vol = services.maximum_buy_volume(
                account_balances=api_services.account_balances(),
                price=new_limit_price,
                precision=5,
            )

            # Create a limit buy order
            new_order = api_services.add_order(
                ordertype="limit",
                type="buy",
                volume=max_buy_vol,
                pair="BTC/USD",
                price=str(new_limit_price),
            )
