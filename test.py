import unittest

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
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)