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

def order_book(pair):
    """
    Retrieve order book for a given asset pair.

    Example:
        >>> order_book("BTC/USD")
    """
    response = kraken_auth.request(
        method="GET",
        path="/0/public/Depth",
        query={
            "pair": pair,
            "count": 10,
        },
        environment="https://api.kraken.com",
    )

    return json.loads(response.read().decode('utf-8'))

def add_order(ordertype, type, volume, pair, price):
    """
    Place a new order.

    Official docs: https://docs.kraken.com/api/docs/rest-api/add-order

    Examples:
        >>> add_order(
                ordertype="limit",
                type="buy",
                volume="1",
                pair="BTC/USD",
                price="1"
            )
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

def cancel_all_orders():
    """Cancel all open orders."""
    response = kraken_auth.request(
      method="POST",
      path="/0/private/CancelAll",
      public_key=public_key,
      private_key=private_key,
      environment="https://api.kraken.com",
    )

    return json.loads(response.read().decode('utf-8'))

def cancel_last_open_order(txid):
    """Cancel last open order."""
    response = kraken_auth.request(
        method="POST",
        path="/0/private/CancelOrder",
        body={
            "txid": "OZUCWN-2ZS5T-JN2VN6",
        },
        public_key="",
        private_key="",
        environment="https://api.kraken.com",
    )

    return json.loads(response.read().decode('utf-8'))
