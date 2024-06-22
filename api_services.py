import os
import requests
import time

from datetime import datetime

import kraken_auth

# Retrieve account balances for all assets
def account_balances():
    print(f'{datetime.now()} Requesting account balances...')
    res_acc_bal = kraken_auth.kraken_request(
        '/0/private/Balance',
        {
            "nonce": str(int(1000*time.time()))
        },
    )
    print(f'{datetime.now()} Request for account balances sent.')
    # print(f'{datetime.now()} Account balances:\n{res_acc_bal.json()}')
    return res_acc_bal.json()

# Retrieve full trade history
def trade_history():
    print(f'{datetime.now()} Requesting trade history...')
    res_trade_history = kraken_auth.kraken_request(
        '/0/private/TradesHistory',
        {
            "nonce": str(int(1000*time.time()))
        },
    )
    print(f'{datetime.now()} Request for trade history sent.')
    # print(f'{datetime.now()} Trade history:\n{res_trade_history.json()}')
    return res_trade_history.json()

# Retrieve active order book for a given asset pair
def order_book(pair):
    print(f'{datetime.now()} Requesting order book...')
    res_order_book = requests.get(f'https://api.kraken.com/0/public/Depth?pair={pair}')
    print(f'{datetime.now()} Request for order book ({pair}) sent.')
    # print(f'{datetime.now()} Order book ({pair}):\n{res_order_book.json()}')
    return res_order_book.json()

# Create a new order
def add_order(order_type, direction, volume, pair):
    print(f'{datetime.now()} Sending trade request...')
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
    print(f'{datetime.now()} Trade request sent.')
    # print(f'{datetime.now()} Trade response:\n{res_add_order.json()}')
    return res_add_order.json()
