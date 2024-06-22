import api_services

# Generate a cleaned list of sorted bid or ask orders
def clean_order_book(pair, direction, expected_trade_volume):
    kraken_identifier = f'X{pair[:3]}Z{pair[3:]}'
    order_book = api_services.order_book(pair)
    cleaned_order_book = []
    cumulative_trade_volume = 0.0

    # Retrieve bid or ask order book
    if direction == 'buy':
        order_book = order_book['result'][kraken_identifier]['asks']
    elif direction == 'sell':
        order_book = order_book['result'][kraken_identifier]['bids']
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

# def active_net_cost(order_book, quantity):
#     pass