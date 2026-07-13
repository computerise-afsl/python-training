#!/usr/bin/env python3
"""Core data types and collections (README Part 2.2)."""


def main():
    # Core types
    count = 5  # int
    price = 19.99  # float
    ticker = "AAPL"  # str
    is_active = True  # bool
    note = None  # None

    print(f"{ticker} costs {price} and is active: {is_active}")

    # Collections
    employees = [
        {"name": "Alice", "department": "Sales", "salary": 52000},
        {"name": "Bob", "department": "Engineering", "salary": 68000},
        {"name": "Carol", "department": "Engineering", "salary": 71000},
        {"name": "Dave", "department": "Sales", "salary": 49000},
    ]

    # Filter: only engineers
    engineers = [e for e in employees if e["department"] == "Engineering"]

    # Transform: just the names
    engineer_names = [e["name"] for e in engineers]

    print("Engineers:", engineer_names)

    # dict, tuple, set
    departments = {"Sales", "Engineering"}
    first_last = ("Alice", "Dave")
    salary_by_name = {e["name"]: e["salary"] for e in employees}

    print("Departments:", departments)
    print("Salary lookup:", salary_by_name)


if __name__ == "__main__":
    main()
