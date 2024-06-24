import unittest

import trader

class TestTrader(unittest.TestCase):
    def setUp(self):
        self.raw_order_book = {
            "error": [],
            "result": {
                "XXBTZUSD": {
                    "asks": [
                        ["60000.50", "1.0"],
                        ["60000.60", "0.5"],
                        ["60000.70", "1.5"],
                    ],
                    "bids": [
                        ["60000.40", "1.0"],
                        ["60000.30", "0.5"],
                        ["60000.20", "1.5"],
                    ],
                },
            },
        }

        self.cleaned_order_book_bids = [
            [60000.40, 1.0],
            [60000.30, 0.5],
            [60000.20, 1.5],
        ]

        self.cleaned_order_book_asks = [
            [60000.50, 1.0],
            [60000.60, 0.5],
            [60000.70, 1.5],
        ]

        self.trading_fee = 0.004
        self.required_return = 0.001

    def test_clean_order_book(self):
        cleaned_order_book_bids = trader.clean_order_book(
            raw_order_book=self.raw_order_book,
            kraken_pair_id="XXBTZUSD",
            direction="buy",
            expected_vol=1.25,
        )
        expected_cleaned_order_book_bids = [
            [60000.40, 1.0],
            [60000.30, 0.5],
        ]
        self.assertEqual(cleaned_order_book_bids, expected_cleaned_order_book_bids)

        cleaned_order_book_asks = trader.clean_order_book(
            raw_order_book=self.raw_order_book,
            kraken_pair_id="XXBTZUSD",
            direction="sell",
            expected_vol=1.25,
        )
        expected_cleaned_order_book_asks = [
            [60000.50, 1.0],
            [60000.60, 0.5],
        ]
        self.assertEqual(cleaned_order_book_asks, expected_cleaned_order_book_asks)

    def test_last_trade_real_time_net_cost(self):
        last_buy_real_time_net_cost = trader.last_trade_real_time_net_cost(
            cleaned_order_book=self.cleaned_order_book_bids,
            last_trade_vol=2.0
        )
        expected_last_buy_real_time_net_cost = 120000.65 * (1 - self.trading_fee)
        self.assertEqual(last_buy_real_time_net_cost, expected_last_buy_real_time_net_cost)

        last_sell_real_time_net_cost = trader.last_trade_real_time_net_cost(
            cleaned_order_book=self.cleaned_order_book_asks,
            last_trade_vol=2.0
        )
        expected_last_sell_real_time_net_cost = 120001.15 * (1 - self.trading_fee)
        self.assertEqual(last_sell_real_time_net_cost, expected_last_sell_real_time_net_cost)

    def test_crosses_trading_threshold(self):
        self.assertTrue(
            trader.crosses_trading_threshold(
                last_trade_net_cost=120000.0,
                last_trade_real_time_net_cost=1200120.1,
                direction='buy',
                required_return=self.required_return
            )
        )
        self.assertFalse(
            trader.crosses_trading_threshold(
                last_trade_net_cost=120000.0,
                last_trade_real_time_net_cost=120119.9,
                direction='buy',
                required_return=self.required_return
            )
        )
        self.assertTrue(
            trader.crosses_trading_threshold(
                last_trade_net_cost=120000.0,
                last_trade_real_time_net_cost=119879.9,
                direction='sell',
                required_return=self.required_return
            )
        )
        self.assertFalse(
            trader.crosses_trading_threshold(
                last_trade_net_cost=120000.0,
                last_trade_real_time_net_cost=119880.1,
                direction='sell',
                required_return=self.required_return
            )
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)
