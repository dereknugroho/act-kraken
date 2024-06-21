import api_services

# def asset_live_market_value(pair, direction):
#     kraken_identifier = f'X{pair[:3]}Z{pair[3:]}'
#     order_book = api_services.order_book(pair)

#     if direction == 'buy':
#         order_book = order_book['result'][kraken_identifier]['asks']
#     elif direction == 'sell':
#         order_book = order_book['result'][kraken_identifier]['bids']

#     print(order_book)
