import api_services

TRADING_FEE = 0.004

# Generate a cleaned list of sorted bid or ask orders
def clean_order_book(raw_order_book, kraken_pair_id, direction, expected_vol):
    cleaned_order_book = []
    cumulative_trade_vol = 0.0

    # Retrieve bid or ask order book
    if direction == 'buy':
        raw_order_book = raw_order_book['result'][kraken_pair_id]['bids']
    elif direction == 'sell':
        raw_order_book = raw_order_book['result'][kraken_pair_id]['asks']
    else:
        raise ValueError('direction argument must be "buy" or "sell"')

    # Generate clean order book
    for raw_order in raw_order_book:
        cleaned_order = []
        cleaned_order.append(float(raw_order[0]))
        cleaned_order.append(float(raw_order[1]))
        cleaned_order_book.append(cleaned_order)
        cumulative_trade_vol += float(raw_order[1])

        if cumulative_trade_vol > expected_vol:
            break
    
    return cleaned_order_book

# Calculate the real-time net cost of the previous trade
def last_trade_real_time_net_cost(cleaned_order_book, last_trade_vol):
    real_time_cost = 0.0
    cumulative_order_vol = 0.0

    for order in cleaned_order_book:
        cumulative_order_vol += order[1]
        if cumulative_order_vol <= last_trade_vol:
            real_time_cost += (order[1] * order[0])
        else:
            excess_trade_vol = last_trade_vol - cumulative_order_vol + order[1]
            real_time_cost += (excess_trade_vol * order[0])
            break

    return real_time_cost * (1 - TRADING_FEE)

# Check if the real-time net cost of the last trade exceeds the trading threshold
def crosses_trading_threshold(last_trade_net_cost, last_trade_real_time_net_cost, direction, required_return):
    if direction == 'buy':
        return last_trade_real_time_net_cost >= ((1 + required_return) * last_trade_net_cost)
    elif direction == 'sell':
        return last_trade_real_time_net_cost <= ((1 - required_return) * last_trade_net_cost)
