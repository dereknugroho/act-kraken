import os

import api_services, trader

if __name__ == '__main__':
    # base_url = 'https://api.kraken.com'
    # key = os.environ['API_KEY_KRAKEN']
    # sec = os.environ['API_SEC_KRAKEN']

    ###########################
    # Test: trading algorithm #
    ###########################

    # trader.asset_live_market_value(
    #     'XBTCAD',
    #     'buy'
    # )

    #########################################
    # Test (API calls): non-trade execution #
    #########################################

    # api_services.account_balances()
    # api_services.trade_history()
    # api_services.order_book('XBTUSD')

    #####################################
    # Test (API calls): trade execution #
    #####################################

    # order_type = 'market'
    # direction = 'buy'
    # volume = 0.0005
    # pair = 'XBTUSD'

    # api_services.add_order(
    #     order_type,
    #     direction,
    #     volume,
    #     pair,
    # )
