#!/usr/bin/env python3
"""Functions: params, defaults, *args/**kwargs, type hints (README Part 2.4)."""


def band_for_salary(
    salary: int, senior_threshold: int = 70000, mid_threshold: int = 55000
) -> str:
    """Return a salary band, using default thresholds unless overridden."""
    if salary >= senior_threshold:
        return "senior"
    if salary >= mid_threshold:
        return "mid"
    return "junior"


def summarise_employees(*names: str, **extra_info: str) -> None:
    """Demonstrate *args (names) and **kwargs (arbitrary extra info)."""
    print("Employees:", ", ".join(names))
    for key, value in extra_info.items():
        print(f"{key}: {value}")


def main():
    employees = [
        {"name": "Alice", "salary": 52000},
        {"name": "Bob", "salary": 68000},
        {"name": "Carol", "salary": 71000},
    ]

    for employee in employees:
        band = band_for_salary(employee["salary"])
        print(f"{employee['name']}: {band}")

    # Override a default via keyword argument
    print(
        "Carol (stricter threshold):",
        band_for_salary(employee["salary"], senior_threshold=75000),
    )

    summarise_employees("Alice", "Bob", "Carol", team="Engineering", quarter="Q3")


if __name__ == "__main__":
    main()
