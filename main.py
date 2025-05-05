import api_services
from datetime import datetime

REQUIRED_RETURN = 0.0001

"""
- If latest order is not an outstanding limit order
- Place market buy order
- Confirm market buy order
- Calculate net cost of latest market buy order
- Calculate required price of limit sell order
  for net cost to return 1 basis point
  given same volume in latest market buy order
- Place limit order based on price of latest market order
"""

def main():
    last_trade = next(iter(api_services.trade_history()['result']['trades'].items()))[1]
    # print(f"Trade history: {api_services.trade_history()['result']['trades']}")
    # print(f'Most recent trade: {last_trade}')
    # print(f'Account balances: {api_services.account_balances()}')
    # print(f'Open orders: {api_services.open_orders()}')

    # Test: place limit order that is unlikely to be filled
    # [May 4, 2025 @ PM] Limit buy order was executed
    # print(f'Executing limit buy order @ {datetime.now()}')
    # api_services.add_order(
    #     order_type='limit',
    #     direction='buy',
    #     price=1,
    #     volume=1,
    #     pair='XBTUSD'
    # )

    # [April 23, 2025 @ 2:38 PM] Limit buy order was executed
    # api_services.add_order(
    #     order_type='limit',
    #     direction='buy',
    #     price=93875.1,
    #     volume=0.0010652,
    #     pair='XBTUSD'
    # )

    # [April 23, 2025 @ 2:48 PM] Limit sell order was executed
    # api_services.add_order(
    #     order_type='limit',
    #     direction='sell',
    #     price=93875.1,
    #     volume=0.0010652,
    #     pair='XBTUSD'
    # )

if __name__ == '__main__':
    main()