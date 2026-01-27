# Python Basics – Bootcamp Exercises

This repository contains a set of introductory Python exercises completed as part of a software development bootcamp. The focus of this project is on setting up a professional Python development environment and understanding common developer workflows.

## Exercises Covered

### 1. Python Environment Inspection
- Created a Python script that imports the `sys` module
- Printed the Python version and executable path
- Ran the script from the command line to confirm the active virtual environment

### 2. Virtual Environments and Package Management
- Created a new project folder
- Set up and activated a Python virtual environment (`.venv`)
- Installed the `requests` package using `pip`
- Verified installed packages using `pip freeze`

### 3. Linting with Pylint
- Configured VS Code to use Pylint
- Created a script with an unused variable
- Observed linting warnings in the VS Code Problems tab

### 4. Formatting on Save with autopep8
- Configured VS Code to automatically format Python files on save
- Installed and used `autopep8` as the Python code formatter
- Verified formatting is applied consistently when files are saved

### 5. Virtual Environment Detection Script
- Created a script to detect whether Python is running inside a virtual environment
- Compared `sys.prefix` and `sys.base_prefix` to determine the execution context
- Printed different messages depending on whether a virtual environment is active

### 6. Formatter and Execution Workflow (UML)
- Created a UML sequence diagram illustrating:
  - Writing code in VS Code
  - Automatic formatting with autopep8 on save
  - Running the script in the integrated terminal
 
### 7. Mutable vs Immutable Data Types
- Explored how Python handles mutable and immutable data types
- Observed object identity changes using `id()`
- Compared reassignment behavior for immutable types (string, int, float, tuple, range, bool)
- Discussed how immutability affects memory usage and variable references

## Tools and Technologies
- Python
- Virtual Environments (`venv`)
- VS Code
- Pylint
- autopep8
- Git & GitHub

## Notes
- The virtual environment (`.venv`) is excluded from version control using `.gitignore`
- VS Code project-specific settings are included to ensure consistent linting and formatting behaviour

---

This project demonstrates basic Python tooling, environment setup, and development workflows commonly used in professional software development.
