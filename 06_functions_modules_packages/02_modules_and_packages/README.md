# Practice — Modules and Packages

This folder contains exercises, lab work, assignments, and short answer questions for the Modules and Packages Python module.

---

## Exercises

1. Create a module named `string_utils.py` that contains at least three functions: `reverse_string`, `is_palindrome`, and `count_vowels`. Then, create a separate script that imports this module and uses all three functions on a user-provided string.

2. Create a package named `simple_project` with two modules: `data_processor.py` and `report_generator.py`. The `data_processor` module should contain a function to read a list of numbers from a text file. The `report_generator` module should contain a function to calculate the average of a list of numbers and write a report to a new file. Create a main script that imports and uses these modules to perform the entire process.

3. Write a script that uses the `requests` module to fetch data from a public API (e.g., a simple weather API). Create a module named `api_client.py` that handles the API request logic and returns the data. Your main script should import `api_client` and display the retrieved data in a clean format.


## Lab Work

**Individual Lab**: Personal Library. Create a personal Python package named `my_library`. Within this package, create at least three modules for different purposes (e.g., `file_helpers`, `web_scrapers`, `data_analyzers`). Populate each module with at least two functions. Then, create a `tests` directory within your project to practice importing and testing your library's functions.

**Team Lab**: Collaborative Package Development. In a team of 3, design and develop a package for a simple, fictitious company. One team member will create the data sub-package for data handling, another will create the logic sub-package for business logic, and the third will create the interface sub-package for user interaction. Each member should be responsible for their sub-package and its modules. The final goal is to integrate all three parts into a single, functional application.



## Assignment

You are tasked with creating a reusable logging package for your organization.

The package, named `org_log`, should have two modules: `log_setup.py` and `log_writer.py`.

The `log_setup` module should contain a function to configure the logger.

The `log_writer` module should have functions for writing informational, warning, and error messages to a file.

Ensure the package can be imported and used by a separate main script.
