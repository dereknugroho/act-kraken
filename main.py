import os

import api_services, trader

EXPECTED_TRADE_VOLUME = 0.0005
REQUIRED_RETURN = 0.001

def main():
    # Calculate net cost of last trade
    trade_history = api_services.trade_history()['result']['trades'].items()
    last_trade = next(iter(trade_history))[1]
    direction = last_trade['type']
    last_trade_net_cost = float(last_trade['cost']) - float(last_trade['fee'])
    print(f'[main()] last_trade_net_cost: {last_trade_net_cost}')

    # Obtain order book
    cleaned_order_book = trader.clean_order_book(
        pair=last_trade['pair'][1:4] + last_trade['pair'][5:8],
        kraken_pair_id=last_trade['pair'],
        direction=direction,
        expected_trade_volume=EXPECTED_TRADE_VOLUME
    )
    print(f'[main()] cleaned_order_book: {cleaned_order_book}')

    # Calculate active net cost of last trade
    last_trade_active_net_cost = trader.last_trade_active_net_cost(
        cleaned_order_book,
        float(last_trade['vol'])
    )
    print(f'[main()] last_trade_active_net_cost ({last_trade["type"]}): {last_trade_active_net_cost}')

    # Execute trade if current net cost of last trade crosses threshold
    if trader.crosses_trading_threshold(last_trade_net_cost, last_trade_active_net_cost, direction, REQUIRED_RETURN):
        if direction == 'buy':
            api_services.add_order(
                'market',
                'sell',
                EXPECTED_TRADE_VOLUME,
                pair=last_trade['pair'][1:4] + last_trade['pair'][5:8],
            )
        elif direction == 'sell':
            api_services.add_order(
                'market',
                'buy',
                EXPECTED_TRADE_VOLUME,
                pair=last_trade['pair'][1:4] + last_trade['pair'][5:8],
            )
    else:
        print(f'No trade executed.\nPrevious trade was a {direction} at {last_trade_net_cost}.\nCurrent net cost: {last_trade_active_net_cost}.\nDifference of {((last_trade_active_net_cost - last_trade_net_cost) / last_trade_net_cost) * 100}% does not cross {REQUIRED_RETURN * 100}% threshold.')

if __name__ == '__main__':
    main()

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
    # direction = 'sell'
    # volume = 0.0005
    # pair = 'XBTUSD'

    # api_services.add_order(
    #     order_type,
    #     direction,
    #     volume,
    #     pair,
    # )
