import pytest

import services

def test_last_trade():
    last_trade = services.last_trade()
    last_trade_keys = [
        "ordertxid",
        "postxid",
        "pair",
        "aclass",
        "time",
        "type",
        "ordertype",
        "price",
        "cost",
        "fee",
        "vol",
        "margin",
        "leverage",
        "misc",
        "trade_id",
        "maker",
    ]

    for key in last_trade.keys():
        assert key in last_trade_keys

# def test_maximum_buy_volume():
#     pass

# def test_reduce_trade_volume():
#     pass
