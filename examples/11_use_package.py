#!/usr/bin/env python3
"""Importing from a package: a folder of modules (README Part 2.5)."""

from team_directory import employees, find_employee


def main():
    print(f"All employees: {employees}")

    alice = find_employee("Alice")
    print(f"Found: {alice}")

    missing = find_employee("Zoe")
    print(f"Missing: {missing}")


if __name__ == "__main__":
    main()
