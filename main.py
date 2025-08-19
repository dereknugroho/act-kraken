import services
import trade_engine

def main():
    trade_engine.trade(services.last_trade())

if __name__ == '__main__':
    main()
