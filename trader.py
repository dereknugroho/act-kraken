MAKER_FEE = 0.0025
TAKER_FEE = 0.004

# # Generate a cleaned list of sorted bid or ask orders
# def clean_order_book(raw_order_book, kraken_pair_id, last_trade_direction, expected_vol):
#     cleaned_order_book = []
#     cumulative_trade_vol = 0.0

#     # Retrieve bid or ask order book
#     if last_trade_direction == 'buy':
#         raw_order_book = raw_order_book['result'][kraken_pair_id]['bids']
#     elif last_trade_direction == 'sell':
#         raw_order_book = raw_order_book['result'][kraken_pair_id]['asks']
#     else:
#         raise ValueError('last_trade_direction argument must be "buy" or "sell"')

#     # Generate clean order book
#     for raw_order in raw_order_book:
#         cleaned_order = []
#         cleaned_order.append(float(raw_order[0]))
#         cleaned_order.append(float(raw_order[1]))
#         cleaned_order_book.append(cleaned_order)
#         cumulative_trade_vol += float(raw_order[1])

#         if cumulative_trade_vol > expected_vol:
#             break
    
#     return cleaned_order_book
