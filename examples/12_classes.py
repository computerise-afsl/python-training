#!/usr/bin/env python3
"""Classes and objects (README Part 2.6)."""


class Trade:
    def __init__(self, ticker, quantity, price):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

    def notional_value(self):
        return self.quantity * self.price


def main():
    trade = Trade("AAPL", 100, 189.50)

    print(trade.ticker)
    print(trade.notional_value())


if __name__ == "__main__":
    main()


# Bonus: a dataclass gives you a similar class with less code to write.
# Worth knowing exists, but not something you need today.
#
# from dataclasses import dataclass
#
# @dataclass
# class TradeRecord:
#     ticker: str
#     quantity: int
#     price: float
