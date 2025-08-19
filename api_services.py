import json
import os

import kraken_auth

public_key = os.environ['API_KEY_KRAKEN']
private_key = os.environ['API_SEC_KRAKEN']

def account_balances():
    """Retrieve account balances for all assets."""
    response = kraken_auth.request(
        method="POST",
        path="/0/private/Balance",
        public_key=public_key,
        private_key=private_key,
        environment="https://api.kraken.com",
    )

    return json.loads(response.read().decode('utf-8'))

def trade_history():
    """Retrieve full trade history."""
    response = kraken_auth.request(
        method="POST",
        path="/0/private/TradesHistory",
        public_key=public_key,
        private_key=private_key,
        environment="https://api.kraken.com",
    )

    return json.loads(response.read().decode('utf-8'))

def add_order(ordertype: str, type: str, volume: str, pair: str, price: str):
    """
    Place a new order.

    Example:
    >>> add_order(
    ...     ordertype="limit",
    ...     type="buy",
    ...     volume="1",
    ...     pair="BTC/USD",
    ...     price="1",
    ... )
    """
    response = kraken_auth.request(
        method="POST",
        path="/0/private/AddOrder",
        body={
            "ordertype": ordertype,
            "type": type,
            "volume": volume,
            "pair": pair,
            "price": price,
        },
        public_key=public_key,
        private_key=private_key,
        environment="https://api.kraken.com",
    )

    return json.loads(response.read().decode('utf-8'))

def open_orders():
    """Retrieve all open orders."""
    response = kraken_auth.request(
        method="POST",
        path="/0/private/OpenOrders",
        public_key=public_key,
        private_key=private_key,
        environment="https://api.kraken.com",
    )

    return json.loads(response.read().decode('utf-8'))

def cancel_all_open_orders():
    """Cancel all open orders."""
    response = kraken_auth.request(
      method="POST",
      path="/0/private/CancelAll",
      public_key=public_key,
      private_key=private_key,
      environment="https://api.kraken.com",
    )

    return json.loads(response.read().decode('utf-8'))

def cancel_open_order(txid: str):
    """
    Cancel an open order.

    Example:
    >>> cancel_order(txid="OZUCWN-2ZS5T-JN2VN6")
    """
    response = kraken_auth.request(
        method="POST",
        path="/0/private/CancelOrder",
        body={
            "txid": txid,
        },
        public_key=public_key,
        private_key=private_key,
        environment="https://api.kraken.com",
    )

    return json.loads(response.read().decode('utf-8'))

def trade_volume(pair: str):
    """
    Get 30 day USD trading volume and fee schedule for
    a given asset pair (e.g. BTC/USD).

    Example:
    >>> trade_volume(pair="BTC/USD")
    """
    response = kraken_auth.request(
        method="POST",
        path="/0/private/TradeVolume",
        body={
            "pair": "BTC/USD"
        },
        public_key=public_key,
        private_key=private_key,
        environment="https://api.kraken.com",
    )

    return json.loads(response.read().decode('utf-8'))
