import trader

REQUIRED_RETURN = 0.0001

def main():
    last_trade = trader.last_trade()

    if last_trade["type"] == "buy":
        new_limit_sell_price = trader.new_limit_sell_price(last_trade, REQUIRED_RETURN)
        new_limit_sell_order = api_services.add_order(
            ordertype="limit",
            type="sell",
            volume=last_trade["vol"],
            pair=last_trade["pair"],
            price=new_limit_sell_price
        )
    elif last_trade["type"] == "sell":
        pass

if __name__ == '__main__':
    main()
