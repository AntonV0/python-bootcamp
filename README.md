# Python Basics – Bootcamp Exercises

This repository contains a set of introductory Python exercises completed as part of a software development bootcamp. The project focuses on Python core data types, virtual environments, developer tooling, and common workflows used in professional development.

## Exercises Covered

### 1. Python Environment Inspection
- Created a Python script that imports the `sys` module
- Printed the Python version and executable path
- Confirmed the active virtual environment from the command line

### 2. Virtual Environments and Package Management
- Created and activated a Python virtual environment (`.venv`)
- Installed third-party packages using `pip`
- Generated and shared dependencies using `requirements.txt`
- Simulated a team workflow using `pip freeze` and `pip install -r`

### 3. Linting and Formatting
- Configured VS Code to use Pylint for static code analysis
- Observed warnings for unused variables and missing docstrings
- Enabled automatic formatting on save using autopep8

### 4. Virtual Environment Detection
- Created a script to detect whether Python is running inside a virtual environment
- Compared `sys.prefix` and `sys.base_prefix` to determine execution context

### 5. Formatter and Execution Workflow (UML)
- Created a UML sequence diagram illustrating:
  - Writing code in VS Code
  - Automatic formatting on save
  - Executing Python scripts in the integrated terminal

### 6. Core Python Data Types
- Explored Python core data types including:
  - `int`, `float`, `str`, `bool`
  - `tuple`, `range`
  - `list`, `dict`, `set`
- Used `type()` and `id()` to inspect object identity and behaviour

### 7. Mutable vs Immutable Data Types
- Investigated immutable data types (`str`, `int`, `float`, `tuple`, `range`, `bool`)
- Observed how reassignment creates new objects for immutable types
- Explored mutable data types (`list`, `dict`, `set`)
- Demonstrated in-place mutation and shared references
- Compared assignment vs object duplication using `.copy()`

### 8. Collections and Set Operations
- Worked with dictionaries to store and update key–value pairs
- Explored sets and their properties (uniqueness, membership testing)
- Used set operators:
  - Union (`|`)
  - Intersection (`&`)
  - Difference (`-`)

## Tools and Technologies
- Python
- Virtual Environments (`venv`)
- pip
- VS Code
- Pylint
- autopep8
- Git & GitHub

## Notes
- The virtual environment (`.venv`) is excluded from version control using `.gitignore`
- Project-specific VS Code settings are included to ensure consistent linting and formatting behaviour

---

This project demonstrates foundational Python concepts, object behaviour, and development workflows commonly used in professional software development.
