import api_services

EXPECTED_TRADE_VOLUME = 0.0015  # Change EXPECTED_TRADE_VOLUME according to Step 1. under Usage in README.md
REQUIRED_RETURN = 0.0001

def main():
    # last_trade = next(iter(api_services.trade_history()['result']['trades'].items()))[1]
    # print(f'Most recent trade: {last_trade}')
    # print(f'Account balances (before limit order): {api_services.account_balances()}')

    # [April 23, 2025 @ 2:38 PM] Limit order buy below was executed
    # api_services.add_order(
    #     order_type='limit',
    #     direction='buy',
    #     price=93875.1,
    #     volume=0.0010652,
    #     pair='XBTUSD'
    # )

    # [April 23, 2025 @ 2:48 PM] Limit order below was executed
    # api_services.add_order(
    #     order_type='limit',
    #     direction='sell',
    #     price=93875.1,
    #     volume=0.0010652,
    #     pair='XBTUSD'
    # )

    print(f'Account balances: {api_services.account_balances()}')

    print(f'Open orders: {api_services.open_orders()}')

    # print(f'Account balances (after limit order): {api_services.account_balances()}')

if __name__ == '__main__':
    main()