"""One module inside the team_directory package (README Part 2.5)."""

employees = [
    {"name": "Alice", "salary": 52000},
    {"name": "Bob", "salary": 68000},
    {"name": "Carol", "salary": 71000},
]


def find_employee(name):
    for employee in employees:
        if employee["name"] == name:
            return employee
    return None
