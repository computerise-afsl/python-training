#!/usr/bin/env python3
"""Tests for payroll_utils.py, run with `pytest` (README Part 2.7).

Note the test_*.py naming convention is what pytest looks for during
discovery; this file breaks that convention slightly (numbered like the
other examples) so run it explicitly with `pytest 13_test_examples.py`.
"""

from payroll_utils import salary_band, total_payroll


def test_salary_band_senior():
    assert salary_band(75000) == "senior"


def test_salary_band_junior():
    assert salary_band(50000) == "junior"


def test_total_payroll():
    employees = [{"salary": 50000}, {"salary": 60000}]
    assert total_payroll(employees) == 110000
