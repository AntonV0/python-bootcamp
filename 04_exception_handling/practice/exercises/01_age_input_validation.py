"""Exercise 1: Age Input Validation"""

def get_valid_age():
    """Prompt the user to enter their age and validate the input.

    The function will keep asking for input until a valid age
    is provided. It returns the valid age as an integer.
    """
    while True:
        age_input = input("Please enter your age: ")
        try:
            age = int(age_input) # Convert input to integer
            if age < 0:
                print("Age cannot be negative. Please try again.")
            elif age > 120:
                print("Age is too high. Please enter a valid age.")
            elif age < 18:
                print("You must be at least 18 years old.")
            else:
                return age
       # Keep asking until valid input is received
        except ValueError: # Handle non-integer inputs
            print("Invalid input. Please enter a valid integer for your age.")

valid_age = get_valid_age()
print(f"Your age is: {valid_age}")

# Example output:
# Please enter your age: abc
# Invalid input. Please enter a valid integer for your age.
# Attempted to read age input.
# Please enter your age: -5
# Age cannot be negative. Please try again.
# Attempted to read age input.
# Please enter your age: 150
# Age is too high. Please enter a valid age.
# Attempted to read age input.
# Please enter your age: 31
# Your valid age is: 31
