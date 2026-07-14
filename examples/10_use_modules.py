#!/usr/bin/env python3
"""Importing your own module, and a quick look at the standard library (README Part 2.5)."""

import json
import os
from datetime import date
from pathlib import Path

from payroll_utils import salary_band, total_payroll


def main():
    employees = [
        {"name": "Alice", "salary": 52000},
        {"name": "Bob", "salary": 68000},
        {"name": "Carol", "salary": 71000},
    ]

    for employee in employees:
        print(f"{employee['name']}: {salary_band(employee['salary'])}")

    print(f"Total payroll: {total_payroll(employees)}")

    # os: ask the operating system a question
    print(f"Current folder: {os.getcwd()}")

    # pathlib: build a file path that works on Mac, Linux and Windows
    report_path = Path("output") / "payroll_report.txt"
    print(f"Report would be saved to: {report_path}")

    # datetime: today's date
    print(f"Today is {date.today()}")

    # json: turn a dict into text you could save to a file
    print(json.dumps(employees[0]))


if __name__ == "__main__":
    main()
