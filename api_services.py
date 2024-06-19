import os
import requests
import time

from datetime import datetime

import kraken_auth

# Retrieve account balances for all assets
def account_balances(api_info):
    print(f'{datetime.now()} Requesting account balances...')
    res_acc_bal = kraken_auth.kraken_request(
        api_info['url'],
        '/0/private/Balance',
        {
            "nonce": str(int(1000*time.time()))
        },
        api_info['key'],
        api_info['sec']
    )
    print(f'{datetime.now()} Request for account balances sent.')
    print(f'{datetime.now()} Account balances:\n{res_acc_bal.json()}')

# Retrieve full trade history
def trade_history(api_info):
    print(f'{datetime.now()} Requesting trade history...')
    res_trade_history = kraken_auth.kraken_request(
        api_info['url'],
        '/0/private/TradesHistory',
        {
            "nonce": str(int(1000*time.time()))
        },
        api_info['key'],
        api_info['sec']
    )
    print(f'{datetime.now()} Request for trade history sent.')
    print(f'{datetime.now()} Trade history:\n{res_trade_history.json()}')

# Retrieve active order book for a given asset pair
def order_book(api_info, pair):
    print(f'{datetime.now()} Requesting order book...')
    res_order_book = requests.get(f'{api_info["url"]}/0/public/Depth?pair={pair}')
    print(f'{datetime.now()} Request for order book ({pair}) sent.')
    print(f'{datetime.now()} Order book ({pair}):\n{res_order_book.json()}')

# Create a new order
def add_order(api_info, order_info):
    print(f'{datetime.now()} Sending trade request\n{order_info}\n...')
    res_add_order = kraken_auth.kraken_request(
        api_info['url'],
        '/0/private/AddOrder',
        {
            "nonce": str(int(1000*time.time())),
            "ordertype": order_info['order_type'],
            "type": order_info['direction'],
            "volume": order_info['volume'],
            "pair": order_info['pair'],
            # "price": order_info['price']
        },
        api_info['key'],
        api_info['sec']
    )
    print(f'{datetime.now()} Trade request sent.')
    print(f'{datetime.now()} Trade response:\n{res_add_order.json()}')
