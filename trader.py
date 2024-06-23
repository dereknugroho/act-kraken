import api_services

# Generate a cleaned list of sorted bid or ask orders
def clean_order_book(pair, kraken_pair_id, direction, expected_trade_volume):
    order_book = api_services.order_book(pair)
    cleaned_order_book = []
    cumulative_trade_volume = 0.0

    # Retrieve bid or ask order book
    if direction == 'buy':
        order_book = order_book['result'][kraken_pair_id]['bids']
    elif direction == 'sell':
        order_book = order_book['result'][kraken_pair_id]['asks']
    else:
        raise ValueError('direction argument must be "buy" or "sell"')

    # Generate clean order book
    for raw_active_order in order_book:
        if cumulative_trade_volume < 1.1 * expected_trade_volume:
            cleaned_active_order = []
            cleaned_active_order.append(float(raw_active_order[0]))
            cleaned_active_order.append(float(raw_active_order[1]))
            cleaned_order_book.append(cleaned_active_order)
            cumulative_trade_volume += float(raw_active_order[1])
        else:
            return cleaned_order_book

def last_buy_active_net_cost(bid_orders, last_trade_vol):
    active_net_cost = 0.0
    cumulative_order_vol = 0.0

    for order in bid_orders:
        cumulative_order_vol += order[1]
        if cumulative_order_vol <= last_trade_vol:
            active_net_cost += (cumulative_order_vol * order[0])
        else:
            excess_trade_volume = last_trade_vol - cumulative_order_vol + order[1]
            active_net_cost += (excess_trade_volume * order[0])
            break

    return active_net_cost