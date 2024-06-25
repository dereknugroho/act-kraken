from datetime import datetime

def write_trade_to_file(trade, account_balances):
    """Append trade details and update account balances to log"""
    trade_time = datetime.fromtimestamp(int(float(trade['time']))).strftime('%b %-d, %Y %-I:%M:%S %p')
    now = datetime.now().strftime('%b %-d, %Y %-I:%M:%S %p')
    direction = trade['type'].capitalize()
    vol = float(trade['vol'])
    coin = trade['pair'][1:4]
    price = float(trade['price'])
    fiat = trade['pair'][5:8]
    net_cost = float(trade['cost']) - float(trade['fee'])

    with open('log.txt', 'a') as file:
        file.write('******************************\n')
        file.write(f'[{trade_time} Atlantic] Trade Executed: {direction} {vol} {coin} at {price} {fiat} (Net {net_cost})\n')
        file.write(f'Balances as of [{now} Atlantic]: {account_balances}\n')
        file.write('******************************\n')
