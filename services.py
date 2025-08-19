import api_services

def last_trade() -> dict:
    """Get details of the last successful trade."""
    return next(iter(api_services.trade_history()["result"]["trades"].items()))[1]

def trading_fee(pair: str, kraken_ticker: str, ordertype: str) -> float:
    """
    Get current maker/taker trading fees.

    Example:
    >>> trading_fee(
    ...     pair="BTC/USD",
    ...     kraken_ticker="XXBTZUSD",
    ...     ordertype="limit",
    ... )
    """
    fee = api_services.trade_volume(pair)["result"]["fees"][kraken_ticker]["fee"]

    if ordertype == "limit":
        fee = api_services.trade_volume(pair)["result"]["fees_maker"][kraken_ticker]["fee"]
        
    return float(fee) / 100

def new_limit_price(last_trade: dict, required_return: float, fee: float) -> float:
    """
    Compute the limit price for a new limit order. The new limit price is
    based on the following:

    1) Last trade price
    2) Trading fee
    3) Required return

    Note: 1% == 0.01

    Example:
    >>> new_limit_price(
    ...     last_trade=helpers.last_trade(),
    ...     required_return=0.0001,
    ...     fee=0.0025,
    ... )
    """
    if last_trade["type"] == "buy":
        return float(last_trade["price"]) * (1 + required_return + fee)
    elif last_trade["type"] == "sell":
        return float(last_trade["price"]) * (1 - fee)

def maximum_buy_volume(account_balances: dict, price: float, precision: int):
    """
    Compute the maximum purchase volume.

    Example:
    >>> maximum_buy_volume(
    ...     account_balances=api_services.account_balances(),
    ...     price=10000.0,
    ...     precision=5
    ... )
    """
    if precision < 0:
        raise ValueError('precision argument must be at least 0.')

    return (1 - 10 ** -precision) * (float(account_balances["result"]["ZUSD"]) / price)
