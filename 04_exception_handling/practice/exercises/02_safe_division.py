"""Exercise 2: Safe Division Function"""

def safe_divide(num1, num2):
    """Perform safe division of two numbers."""
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError: # Handle division by zero
        print("Error: Division by zero is not allowed.")
        return None # Return None to indicate failure
    except TypeError: # Handle non-numeric inputs
        print("Error: Invalid input type. Please provide numbers.")
        return None

print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: Error: Division by zero is not allowed. and None
print(safe_divide(10, 'a'))  # Output: Error: Invalid input type. Please provide numbers. and None
