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
    for raw_active_order in raw_order_book:
        cleaned_active_order = []
        cleaned_active_order.append(float(raw_active_order[0]))
        cleaned_active_order.append(float(raw_active_order[1]))
        cleaned_order_book.append(cleaned_active_order)
        cumulative_trade_vol += float(raw_active_order[1])

        if cumulative_trade_vol > expected_vol:
            break
    
    return cleaned_order_book

# Calculate the current net cost of the previous trade
def last_trade_active_net_cost(cleaned_order_book, last_trade_vol):
    current_net_cost = 0.0
    cumulative_order_vol = 0.0

    for order in cleaned_order_book:
        cumulative_order_vol += order[1]
        if cumulative_order_vol <= last_trade_vol:
            current_net_cost += (cumulative_order_vol * order[0] * (1 - TRADING_FEE))
        else:
            excess_trade_vol = last_trade_vol - cumulative_order_vol + order[1]
            current_net_cost += (excess_trade_vol * order[0] * (1 - TRADING_FEE))
            break

    return current_net_cost

# Check if the active net cost of the last trade exceeds the trading threshold
def crosses_trading_threshold(last_trade_net_cost, last_trade_active_net_cost, direction, required_return):
    if direction == 'buy':
        return last_trade_active_net_cost > ((1 + required_return) * last_trade_net_cost)
    elif direction == 'sell':
        return last_trade_active_net_cost < ((1 - required_return) * last_trade_net_cost)
