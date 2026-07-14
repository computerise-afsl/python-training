#!/usr/bin/env python3
"""Lists and indexing (README Part 2.2)."""


def main():
    departments = ["Sales", "Engineering", "Finance"]

    # Indexing starts at 0, not 1
    print(f"First: {departments[0]}")
    print(f"Second: {departments[1]}")

    # Negative indexes count from the end
    print(f"Last: {departments[-1]}")

    # len() tells you how many items are in the list
    print(f"Count: {len(departments)}")

    # You can change an item by assigning to its index
    departments[0] = "Retail"
    print(f"After change: {departments}")

    # You can add a new item to the end
    departments.append("Marketing")
    print(f"After append: {departments}")


if __name__ == "__main__":
    main()
