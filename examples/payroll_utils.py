#!/usr/bin/env python3
"""A small module of reusable functions (README Part 2.5).

This mirrors the 2.5 exercise: take a function written earlier
(band_for_salary in 6_functions.py) and move it into its own module
so other scripts can import it.
"""


def band_for_salary(
    salary: int, senior_threshold: int = 70000, mid_threshold: int = 55000
) -> str:
    """Return a salary band, using default thresholds unless overridden."""
    if salary >= senior_threshold:
        return "senior"
    if salary >= mid_threshold:
        return "mid"
    return "junior"


def total_payroll(employees: list[dict]) -> int:
    """Sum the salary field across a list of employee dicts."""
    return sum(employee["salary"] for employee in employees)
