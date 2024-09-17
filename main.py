import api_services, helpers, trader

EXPECTED_TRADE_VOLUME = 0.0015
REQUIRED_RETURN = 0.0005

def main():
    last_trade = next(iter(api_services.trade_history()['result']['trades'].items()))[1]

    # Calculate historical net cost of last trade
    last_trade_net_cost = float(last_trade['cost']) - float(last_trade['fee'])
    # print(f'Last trade net cost: {last_trade_net_cost} ({last_trade["type"]} {float(last_trade["vol"])} {last_trade["pair"][1:4]} at {float(last_trade["price"])} {last_trade["pair"][5:8]})')

    # Obtain order book
    last_trade_pair = last_trade['pair'][1:4] + last_trade['pair'][5:8]
    last_trade_direction = last_trade['type']
    cleaned_order_book = trader.clean_order_book(
        raw_order_book=api_services.order_book(pair=last_trade_pair),
        kraken_pair_id=last_trade['pair'],
        last_trade_direction=last_trade_direction,
        expected_vol=EXPECTED_TRADE_VOLUME
    )
    # print(f'Order book: {cleaned_order_book}')

    # Calculate real-time net cost of last trade
    last_trade_real_time_net_cost = trader.last_trade_real_time_net_cost(
        cleaned_order_book=cleaned_order_book,
        last_trade_vol=float(last_trade['vol']),
        last_trade_direction=last_trade_direction
    )
    # print(f'Last trade real-time net cost: {last_trade_real_time_net_cost}')

    # Execute trade if current net cost of last trade crosses threshold
    if trader.crosses_trading_threshold(last_trade_net_cost, last_trade_real_time_net_cost, last_trade_direction, REQUIRED_RETURN):
        if last_trade_direction == 'buy':
            api_services.add_order(
                'market',
                'sell',
                EXPECTED_TRADE_VOLUME,
                pair=last_trade_pair,
            )
        elif last_trade_direction == 'sell':
            api_services.add_order(
                'market',
                'buy',
                EXPECTED_TRADE_VOLUME,
                pair=last_trade_pair,
            )

        # If a trade was executed, append trade details to log
        updated_last_trade = next(iter(api_services.trade_history()['result']['trades'].items()))[1]
        helpers.write_trade_to_file(
            trade=updated_last_trade,
            account_balances=api_services.account_balances()['result']
        )
    else:
        print(f'No trade executed.\nPrevious trade was a {last_trade_direction} at {last_trade_net_cost}.\nCurrent net cost: {last_trade_real_time_net_cost}.\nDifference of {((last_trade_real_time_net_cost - last_trade_net_cost) / last_trade_net_cost) * 100}% does not cross {REQUIRED_RETURN * 100}% threshold.')

if __name__ == '__main__':
    main()

    #########################################
    # Test (API calls): non-trade execution #
    #########################################

    # print(f'Account Balances: {api_services.account_balances()}')
    # print(f'Trade History: {api_services.trade_history()}')
    # api_services.order_book('XBTUSD')

    #####################################
    # Test (API calls): trade execution #
    #####################################

    # order_type = 'market'
    # direction = 'sell'
    # volume = 0.0015
    # pair = 'XBTCAD'

    # api_services.add_order(
    #     order_type,
    #     direction,
    #     volume,
    #     pair,
    # )
