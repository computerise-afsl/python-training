#!/usr/bin/env python3
"""Control flow: if/elif/else, for, while, comprehensions (README Part 2.3)."""


def main():
    employees = [
        {"name": "Alice", "department": "Sales", "salary": 52000},
        {"name": "Bob", "department": "Engineering", "salary": 68000},
        {"name": "Carol", "department": "Engineering", "salary": 71000},
        {"name": "Dave", "department": "Sales", "salary": 49000},
    ]

    # for loop + if/elif/else
    for employee in employees:
        if employee["salary"] >= 70000:
            band = "senior"
        elif employee["salary"] >= 55000:
            band = "mid"
        else:
            band = "junior"
        print(f"{employee['name']}: {band}")

    # while loop
    total = 0
    index = 0
    while index < len(employees):
        total += employees[index]["salary"]
        index += 1
    print("Total payroll:", total)

    # comprehension version of the same filter/transform from 4_data_types.py
    engineer_names = [e["name"] for e in employees if e["department"] == "Engineering"]
    print("Engineers:", engineer_names)


if __name__ == "__main__":
    main()
