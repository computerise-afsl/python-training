#!/usr/bin/env python3
"""Control flow: if/elif/else, for, while (README Part 2.3)."""


def main():
    employees = [
        {"name": "Alice", "salary": 52000},
        {"name": "Bob", "salary": 68000},
        {"name": "Carol", "salary": 71000},
    ]

    # for: do something for every item in a list
    for employee in employees:
        if employee["salary"] >= 70000:
            print(f"{employee['name']} is senior")
        elif employee["salary"] >= 55000:
            print(f"{employee['name']} is mid-level")
        else:
            print(f"{employee['name']} is junior")

    # while: keep going until a condition becomes False
    total = 0
    i = 0
    while i < len(employees):
        total = total + employees[i]["salary"]
        i = i + 1

    print(f"Total payroll: {total}")

    # A comprehension is a short way to write a for loop that builds a list
    names = [employee["name"] for employee in employees]
    print(f"Names: {names}")


if __name__ == "__main__":
    main()
