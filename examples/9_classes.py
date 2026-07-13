#!/usr/bin/env python3
"""Classes and objects, plus a dataclass alternative (README Part 2.6)."""

from dataclasses import dataclass


class Trade:
    """Bundles trade data with the behaviour that acts on it."""

    def __init__(self, ticker: str, quantity: int, price: float):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

    def notional_value(self) -> float:
        return self.quantity * self.price

    def describe(self) -> str:
        return (
            f"{self.quantity} x {self.ticker} @ {self.price} = {self.notional_value()}"
        )


@dataclass
class TradeRecord:
    """Same idea as Trade, but as a lightweight dataclass for simple data."""

    ticker: str
    quantity: int
    price: float

    def notional_value(self) -> float:
        return self.quantity * self.price


def main():
    trade = Trade("AAPL", 100, 189.50)
    print(trade.describe())

    record = TradeRecord("MSFT", 50, 410.25)
    print(record, "-> notional:", record.notional_value())


if __name__ == "__main__":
    main()
