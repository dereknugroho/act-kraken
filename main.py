import os

import api_services, trader

if __name__ == '__main__':
    api_info = {
        'url': 'https://api.kraken.com',
        'key': os.environ['API_KEY_KRAKEN'],
        'sec': os.environ['API_SEC_KRAKEN']
    }

    # order_info = {
    #     'pair': 'XBTCAD',
    #     'direction': 'buy',
    #     'volume': 0.0005,
    #     'order_type': 'market',
    #     'price': None
    # }

    # api_services.account_balances(api_info)
    # api_services.trade_history(api_info)
    # api_services.order_book(api_info, 'XBTCAD')
    # api_services.add_order(api_info, order_info)