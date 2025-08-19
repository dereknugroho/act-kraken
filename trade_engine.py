import api_services
import services

REQUIRED_RETURN = 0.0001

def trade(last_trade: dict) -> dict:
    """
    Implement trading strategy and execute trade.

    Example:
    >>> trade(services.last_trade())
    """

    # Calculate trading fee
    trading_fee = services.trading_fee(
        pair="BTC/USD",
        kraken_ticker=last_trade["pair"],
        ordertype=last_trade["ordertype"],
    )

    # Calculate limit price for new limit order
    new_limit_price = services.new_limit_price(
        last_trade=last_trade,
        required_return=REQUIRED_RETURN,
        fee=trading_fee,
    )

    # Calculate maximum purchase volume
    max_buy_vol = services.maximum_buy_volume(
        account_balances=api_services.account_balances(),
        price=new_limit_price,
        precision=5,
    )

    # Execute trade
    if last_trade["type"] == "buy" and not api_services.open_orders()["result"]["open"]:
        new_order = api_services.add_order(
            ordertype="limit",
            type="sell",
            volume=last_trade["vol"],
            pair="BTC/USD",
            price=str(new_limit_price),
        )
        print(f'New limit sell order has been placed: {new_order}')
    elif last_trade["type"] == "sell" and not api_services.open_orders()["result"]["open"]:
        new_order = api_services.add_order(
            ordertype="limit",
            type="buy",
            volume=max_buy_vol,
            pair="BTC/USD",
            price=str(new_limit_price),
        )
        print(f'New limit buy order has been placed: {new_order}')
