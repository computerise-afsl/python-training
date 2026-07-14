#!/usr/bin/env python3
"""Functions: parameters, default arguments, *args (README Part 2.4)."""


def greet(name):
    print(f"Hello, {name}")


def salary_band(salary, senior_amount=70000):
    """Work out whether a salary counts as senior or junior."""
    if salary >= senior_amount:
        return "senior"
    return "junior"


def add_all(*numbers):
    """*numbers collects any number of arguments into one tuple."""
    total = 0
    for number in numbers:
        total = total + number
    return total


def main():
    greet("Alice")

    print(salary_band(75000))
    print(salary_band(50000))

    # senior_amount has a default, but you can override it
    print(salary_band(65000, senior_amount=60000))

    print(add_all(1, 2, 3, 4))


if __name__ == "__main__":
    main()
