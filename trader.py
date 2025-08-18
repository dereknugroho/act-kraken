import api_services

MAKER_FEE = 0.0025
TAKER_FEE = 0.004

def new_limit_sell_price(last_trade, required_return):
    """
    Compute the limit sell price for a new limit order.

    The new limit sell price is based on the last trade and the required return.
    """
    fee = MAKER_FEE if last_trade["ordertype"] == "limit" else TAKER_FEE

    return float(last_trade["price"]) * (1 + required_return + fee)

def last_trade():
    """Get details of the most recent trade."""
    return next(iter(api_services.trade_history()["result"]["trades"].items()))[1]

def get_last_open_order_id(open_orders):
    """Get ID of the most recently opened open order."""
    return list(open_orders["result"]["open"].keys())[0]

def trading_fee():
    """Calculate trading fee based on 30-day volume."""
    pass
