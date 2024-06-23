import os

import api_services, trader

def main():
    trader.last_trade_net_cost()
    # Calculate net cost of last trade
    # Obtain order book
    # Calculate current net cost of last trade

if __name__ == '__main__':
    main()

    ###########################
    # Test: trading algorithm #
    ###########################

    # print(f"Raw order book *****\n{api_services.order_book('XBTCAD')}")
    # print(f"Cleaned order book *****\n{trader.clean_order_book('XBTCAD', 'sell', 0.5)}")

    #########################################
    # Test (API calls): non-trade execution #
    #########################################

    # print(api_services.account_balances())
    # print(api_services.trade_history())
    # print(api_services.order_book('XBTCAD'))

    #####################################
    # Test (API calls): trade execution #
    #####################################

    # order_type = 'market'
    # direction = 'sell'
    # volume = 0.0005
    # pair = 'XBTUSD'

    # print(
    #     api_services.add_order(
    #         order_type,
    #         direction,
    #         volume,
    #         pair,
    #     )
    # )
