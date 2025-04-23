TRADING_FEE = 0.004

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

# # Calculate the real-time net cost of the previous trade
# def last_trade_real_time_net_cost(cleaned_order_book, last_trade_vol, last_trade_direction):
#     real_time_cost = 0.0
#     cumulative_order_vol = 0.0

#     for order in cleaned_order_book:
#         cumulative_order_vol += order[1]
#         if cumulative_order_vol <= last_trade_vol:
#             real_time_cost += (order[1] * order[0])
#         else:
#             excess_trade_vol = last_trade_vol - cumulative_order_vol + order[1]
#             real_time_cost += (excess_trade_vol * order[0])
#             break

#     if last_trade_direction == 'buy':
#         return real_time_cost * (1 - TRADING_FEE)
#     elif last_trade_direction == 'sell':
#         return real_time_cost * (1 + TRADING_FEE)
#     else:
#         raise ValueError('last_trade_direction argument must be "buy" or "sell"')

# # Check if the real-time net cost of the last trade crosses the trading threshold
# def crosses_trading_threshold(last_trade_net_cost, last_trade_real_time_net_cost, last_trade_direction, required_return):
#     if last_trade_direction == 'buy':
#         return last_trade_real_time_net_cost >= ((1 + required_return) * last_trade_net_cost)
#     elif last_trade_direction == 'sell':
#         return last_trade_real_time_net_cost <= ((1 - required_return) * last_trade_net_cost)
#     else:
#         raise ValueError('last_trade_direction argument must be "buy" or "sell"')
