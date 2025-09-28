from src.trading_services import last_trade
from src.trading_engine import trade

def main(last_trade):
    trade(last_trade)

if __name__ == '__main__':
    main(last_trade())

