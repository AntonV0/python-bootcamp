"""Exercise 3: File Number Reader"""

def read_numbers_from_file(file_path):
    """Read numbers from a file and return them as a list of integers.

    The function handles FileNotFoundError and ValueError.
    """
    numbers = [] # List to store the numbers read from the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  #  Open the file for reading and specify encoding
            for line in file: # Read each line in the file
                try:
                    number = int(line.strip())  # Convert each line to an integer
                    numbers.append(number) # Add the number to the list
                except ValueError:  # Handle non-integer lines
                    print(f"Warning: Invalid number '{line.strip()}' skipped.")
    except FileNotFoundError:  # Handle file not found error
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:  # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")

    return numbers

file_path = 'numbers.txt' # Specify the path to the file
numbers = read_numbers_from_file(file_path) # Read numbers from the file
print(f"Numbers read from file: {numbers}") # Print the list of numbers

# Output if file not found:
# Error: The file 'numbers.txt' was not found.
# Numbers read from file: []

# Output if file found:
# Warning: Invalid number 'This line cannot be converted to a number' skipped.
# Numbers read from file: [1, 2, 3, 4, 5, 6, 7, 8, 9]
