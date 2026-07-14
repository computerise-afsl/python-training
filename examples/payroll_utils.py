#!/usr/bin/env python3
"""A module: code you write once and import into other scripts (README Part 2.5)."""


def salary_band(salary, senior_amount=70000):
    if salary >= senior_amount:
        return "senior"
    return "junior"


def total_payroll(employees):
    total = 0
    for employee in employees:
        total = total + employee["salary"]
    return total
