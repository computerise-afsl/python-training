#!/usr/bin/env python3
"""Core data types and collections (README Part 2.2)."""


def main():
    name = "Alice"  # str
    age = 30  # int
    salary = 52000.50  # float
    is_manager = True  # bool
    promotion_date = None  # no value yet

    print(f"{name} is {age}, earns {salary}, manager: {is_manager}, promoted: {promotion_date}")

    # A list holds many values, in order
    departments = ["Sales", "Engineering", "Finance"]
    print(f"Departments: {departments}")
    print(f"First department: {departments[0]}")

    # A dict holds values looked up by name (a "key")
    employee = {"name": "Alice", "department": "Sales", "salary": 52000}
    print(f"Name: {employee['name']}")
    print(f"Salary: {employee['salary']}")

    # f-strings let you build a message with variables inside it
    print(f"{employee['name']} works in {employee['department']}")


if __name__ == "__main__":
    main()
