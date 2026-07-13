#!/usr/bin/env python3
"""Unit tests for the payroll_utils module, run with `pytest` (README Part 2.7).

Note the test_*.py naming convention is what pytest looks for during
discovery; this file breaks that convention slightly (numbered like the
other examples) so run it explicitly with `pytest 10_test_examples.py`.
"""

from payroll_utils import band_for_salary, total_payroll


def test_band_for_salary_senior():
    assert band_for_salary(70000) == "senior"


def test_band_for_salary_mid():
    assert band_for_salary(60000) == "mid"


def test_band_for_salary_junior():
    assert band_for_salary(30000) == "junior"


def test_total_payroll():
    employees = [{"salary": 50000}, {"salary": 60000}]
    assert total_payroll(employees) == 110000
