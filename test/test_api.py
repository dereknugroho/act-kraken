import pytest

import api_services

def test_account_balances():
    account_balances = api_services.account_balances()["result"]
    assert bool(account_balances)

def test_trade_history():
    trade_history = api_services.trade_history()["result"]
    assert trade_history["count"] > 0
    assert bool(trade_history["trades"])

def test_trade_volume():
    trade_volume_btcusd = api_services.trade_volume("BTC/USD")["result"]
    assert bool(trade_volume_btcusd)
