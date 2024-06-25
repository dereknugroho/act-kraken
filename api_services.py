import requests
import time

from datetime import datetime

import kraken_auth

def account_balances():
    """Retrieve account balances for all assets"""
    res_acc_bal = kraken_auth.kraken_request(
        '/0/private/Balance',
        {
            "nonce": str(int(1000*time.time()))
        },
    )
    # print(f'{datetime.now()} [Kraken API Call] Account balances:\n{res_acc_bal.json()}')
    return res_acc_bal.json()

def trade_history():
    """Retrieve full trade history"""
    res_trade_history = kraken_auth.kraken_request(
        '/0/private/TradesHistory',
        {
            "nonce": str(int(1000*time.time()))
        },
    )
    # print(f'{datetime.now()} [Kraken API Call] Trade history:\n{res_trade_history.json()}')
    return res_trade_history.json()

def order_book(pair):
    """Retrieve real-time order book for a given asset pair"""
    res_order_book = requests.get(f'https://api.kraken.com/0/public/Depth?pair={pair}')
    # print(f'{datetime.now()} [Kraken API Call] Order book ({pair}):\n{res_order_book.json()}')
    return res_order_book.json()

def add_order(order_type, direction, volume, pair):
    """Create a new order"""
    res_add_order = kraken_auth.kraken_request(
        '/0/private/AddOrder',
        {
            "nonce": str(int(1000*time.time())),
            "ordertype": order_type,
            "type": direction,
            "volume": volume,
            "pair": pair,
        },
    )
    # print(f'{datetime.now()} [Kraken API Call] Trade response:\n{res_add_order.json()}')
    return res_add_order.json()
