#!/usr/bin/env python3
"""Stock

Write a test program that creates a Stock object
with the stock symbol INTC, the name Intel Corporation,
the previous closing price of 20.5, and the new
current price of 20.35, and display the price­change
percentage.
"""

class Stock:

    def __init__(self, symbol, name, price_close, price_current):
        self.__symbol = symbol
        self.__name = name
        self.__price_close = price_close
        self.__price_current = price_current

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

    def get_price_close(self):
        return self.__price_close

    def get_price_current(self):
        return self.__price_current

    def set_price_close(self):
        self.__price_close = self.__price_current

    def set_price_current(self, price):
        self.__price_current = price

    def get_change_percent(self):
        percent = self.get_price_close() / self.get_price_current()
        return -(1 - percent)

if __name__ == "__main__":
    stock = Stock("INTC", "Intel Corporation", 20.50, 20.35)
    change = stock.get_change_percent()
    msg = "No changes recorded!"
    if change < 0:
        msg = "This stock has lost {:.2%}".format(change)
    elif change > 0:
        msg = "This stock has gained {:.2%}".format(change)
    print(msg)
