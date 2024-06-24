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

    def test_last_trade_active_net_cost(self):
        pass

    def test_crosses_trading_threshold(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
