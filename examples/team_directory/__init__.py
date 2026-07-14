"""A package: a folder of modules that Python can import as one thing.

What makes this folder a package is this __init__.py file. The real code
lives in directory.py, but re-exporting it here means other scripts can
write `from team_directory import employees` instead of needing to know
that directory.py exists.
"""

from .directory import employees, find_employee
