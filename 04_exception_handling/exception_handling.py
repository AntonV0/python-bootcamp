"""Exception Handling"""

# ? Example of handling exceptions in Python
try:  # This block may raise an exception
    result = 10 / 0  # Division by zero
    # This line will not be executed if an exception occurs
    print("Result:", result)
except ZeroDivisionError as e:  # Catching specific exception
    print("Error: Cannot divide by zero.", e)
except Exception as e:  # Catching any other exceptions
    print("An unexpected error occurred:", e)
finally:  # This block will always execute
    print("Execution completed.")

print(10/0)  # Comment this out to test exception handling code below
# ? Output: ZeroDivisionErrorError: Cannot divide by zero. division by zero


# ? File handling with exception management
FILE_NAME = "exception_handling_file_processing.txt"

F = None
try:
    # Attempt to open a file in read mode
    # Encoding specified for compatibility
    with open(FILE_NAME, "r", encoding="utf-8") as F:
        content = F.read()  # Read file content
        print("The contents of the file are: ", content)
except FileNotFoundError as e:  # Catching file not found exception
    print("Error: The file was not found.", e)
finally:
    if F:
        F.close()  # Ensure the file is closed if it was opened
        print("File closed.")

# exception_handling_file_processing.txt exists in current directory
# ? So, the output will be:
# The contents of the file are:  Tests the error handling using this file and exception_handling.py.
# File closed.

# If the file does not exist, there is no "File closed." message since the file was never opened.
# ? The output will be:
# Error: The file was not found. [Errno 2] No such file or directory:
# 'exception_handling_file_processing.txt'
