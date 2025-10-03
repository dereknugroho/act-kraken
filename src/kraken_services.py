from config.config import config
from config.logging import setup_logger, DEBUG
from src.kraken_client import make_request

# Initialize logger
logger = setup_logger(
    __name__,
    config['logging']['kraken_services_filepath'],
    DEBUG,
)

def account_balances():
    """Retrieve account balances for all assets."""
    return make_request(config["endpoints"]["balances"])

def trade_history():
    """Retrieve full trade history."""
    return make_request(config["endpoints"]["trade_history"])

def add_order(ordertype: str, direction: str, volume: str, pair: str, price: str):
    """
    Place a new order.

    Example:
    >>> add_order(
    ...     ordertype="limit",
    ...     direction="buy",
    ...     volume="1",
    ...     pair="BTC/USD",
    ...     price="1",
    ... )
    """
    body = {
        "ordertype": ordertype,
        "type": direction,
        "volume": volume,
        "pair": pair,
        "price": price,
    }
    return make_request(config["endpoints"]["add_order"], body)

def open_orders():
    """Retrieve all open orders."""
    return make_request(config["endpoints"]["open_orders"])

def cancel_all_open_orders():
    """Cancel all open orders."""
    return make_request(config["endpoints"]["cancel_all"])

def cancel_open_order(txid: str):
    """
    Cancel an open order.

    Example:
    >>> cancel_order(txid="OZUCWN-2ZS5T-JN2VN6")
    """
    body = {"txid": txid}
    return make_request(config["endpoints"]["cancel_order"], body)

def trade_volume(pair: str = "BTC/USD"):
    """
    Get 30 day USD trading volume and fee schedule for
    a given asset pair (e.g. BTC/USD).

    Example:
    >>> trade_volume(pair="BTC/USD")
    """
    body = {"pair": pair}
    return make_request(config["endpoints"]["trade_volume"], body)
