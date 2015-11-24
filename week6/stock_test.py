#!/usr/bin/env python3
import unittest
from stock import Stock


class StockTest(unittest.TestCase):

    def setUp(self):
        self.stock = Stock("INTC", "Intel Corporation", 20.50, 20.35)

    def test_get_name(self):
        self.assertEqual(self.stock.get_name(), self.stock._Stock__name)

    def test_get_symbol(self):
        self.assertEqual(
            self.stock.get_symbol(),
            self.stock._Stock__symbol
        )

    def test_get_price_close(self):
        self.assertEqual(
            self.stock.get_price_close(),
            self.stock._Stock__price_close
        )

    def test_get_price_current(self):
        self.assertEqual(
            self.stock.get_price_current(),
            self.stock._Stock__price_current
        )

    def test_get_change_percent(self):
        percent = self.stock.get_price_close() / \
                  self.stock.get_price_current()
        self.assertEqual(
            self.stock.get_change_percent(),
            -(1 - percent)
        )

if __name__ == "__main__":
    unittest.main()


