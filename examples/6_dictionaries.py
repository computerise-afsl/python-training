#!/usr/bin/env python3
"""Dictionaries and keys (README Part 2.2)."""


def main():
    employee = {"name": "Alice", "department": "Sales", "salary": 52000}

    # Look up a value by its key
    print(f"Name: {employee['name']}")
    print(f"Salary: {employee['salary']}")

    # Add a new key, or update an existing one
    employee["salary"] = 55000
    employee["email"] = "alice@example.com"
    print(f"After update: {employee}")

    # Check whether a key exists before using it
    if "email" in employee:
        print("This employee has an email on file")

    # Loop over every key in the dict
    for key in employee:
        print(f"{key}: {employee[key]}")


if __name__ == "__main__":
    main()
