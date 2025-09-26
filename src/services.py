import math

import src.api_services

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
    trade_volume = api_services.trade_volume(pair)["result"]

    fee = trade_volume["fees"][kraken_ticker]["fee"]
    
    if ordertype == "limit":
        fee = trade_volume["fees_maker"][kraken_ticker]["fee"]
        
    return float(fee) / 100

def new_limit_price(last_trade: dict, required_return: float = 0.0001, fee: float = 0.004) -> float:
    """
    Calculate the limit price of a new limit order. The new limit price is
    based on the following:

    1) Last trade price
    2) Required return
    3) Trading fee

    Note: 1% == 0.01
    Note: return value can be precise only to 10^-1

    Example:
    >>> new_limit_price(
    ...     last_trade=helpers.last_trade(),
    ...     required_return=0.0001,
    ...     fee=0.0025,
    ... )
    """
    if last_trade["type"] == "buy":
        return math.floor(float(last_trade["price"]) * (1 + required_return + fee) * 10) / 10
    elif last_trade["type"] == "sell":
        return math.floor(float(last_trade["price"]) * (1 - fee) * 10) / 10

def maximum_buy_volume(account_balances: dict, price: float, precision: int):
    """
    Calculate the maximum purchase volume at a given price.

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

def reduce_trade_volume(last_trade_volume: float, reduction_factor: float = 0.995):
    """
    Reduce a trade volume in order to ensure sufficient balances for an upcoming limit order.

    Example:
    >>> reduce_trade_volume(last_trade_volume=1.0)
    0.995
    """
    # Ensure reduction factor is within (0, 1)
    if reduction_factor <= 0 or reduction_factor >= 1:
        raise ValueError('reduction_factor must be greater than 0 and less than 1')

    return reduction_factor * last_trade_volume
