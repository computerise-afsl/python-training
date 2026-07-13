#!/usr/bin/env python3
"""Imports, and a quick standard library tour (README Part 2.5)."""

import json
from datetime import date
from pathlib import Path

from payroll_utils import band_for_salary, total_payroll


def main():
    employees = [
        {"name": "Alice", "salary": 52000},
        {"name": "Bob", "salary": 68000},
        {"name": "Carol", "salary": 71000},
    ]

    for employee in employees:
        print(employee["name"], band_for_salary(employee["salary"]))

    print("Total payroll:", total_payroll(employees))

    # pathlib: build a path without worrying about "/" vs "\"
    report_path = Path("output") / "payroll_report.json"
    print("Report would be written to:", report_path)

    # json: serialise the data
    report = {"generated_on": str(date.today()), "employees": employees}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
