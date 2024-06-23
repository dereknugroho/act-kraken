import os

import api_services, trader

EXPECTED_TRADE_VOLUME = 0.0005

def main():
    # Calculate net cost of last trade
    trade_history = api_services.trade_history()['result']['trades'].items()
    last_trade = next(iter(trade_history))[1]
    last_trade_net_cost = float(last_trade['cost']) - float(last_trade['fee'])
    print(f'[main()] last_trade_net_cost: {last_trade_net_cost}')

    # Obtain order book
    cleaned_order_book = trader.clean_order_book(
        pair=last_trade['pair'][1:4] + last_trade['pair'][5:8],
        kraken_pair_id=last_trade['pair'],
        direction=last_trade['type'],
        expected_trade_volume=EXPECTED_TRADE_VOLUME
    )
    print(f'[main()] cleaned_order_book *****\n{cleaned_order_book}')

    # Calculate current net cost of last trade
    if last_trade['type'] == 'buy':
        last_buy_active_net_cost = trader.last_buy_active_net_cost(
            cleaned_order_book,
            float(last_trade['vol'])
        )
        print(f'[main()] last_buy_active_net_cost: {last_buy_active_net_cost}')

    # Execute trade

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

    # api_services.account_balances()
    # api_services.trade_history()
    # api_services.order_book('XBTCAD')

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
