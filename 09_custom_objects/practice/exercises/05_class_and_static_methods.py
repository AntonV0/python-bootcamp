"""Exercise 5: Class and Static Methods"""


class Date:
    """Date class with attributes for day, month, and year."""

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # Static method does not depend on instance or class attributes.
    @staticmethod
    def is_valid_date(day, month, year):
        """Static method to validate a date."""
        if month < 1 or month > 12:  # Check if month is valid
            return False
        if day < 1 or day > 31:  # Check if day is valid
            return False
        if month in [4, 6, 9, 11] and day > 30:  # Check for months with 30 days
            return False
        if month == 2:  # Check for February
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # Check for leap year
                # February has 29 days in a leap year
                # February has 28 days in a non-leap year
                # year % 4 == 0 and year % 100 != 0 checks for leap years ( / by 4 but not by 100)
                # year % 400 == 0 checks for leap years that are divisible by 400
                return day <= 29
            return day <= 28
        return True  # If all checks pass, the date is valid

    # Class method takes the class as the first argument and can access class attributes.
    @classmethod
    def from_string(cls, date_string):
        """Class method to create a Date object from a string."""
        # Order is YYYY-MM-DD
        year, month, day = map(int, date_string.split('-'))
        # Validate the date using the static method
        # cls - references the class itself, so we can call methods without creating an instance
        if cls.is_valid_date(day, month, year):
            # Create and return a Date object if the date is valid
            return cls(day, month, year)

        raise ValueError("Invalid date")


if __name__ == "__main__":
    user_input = input("Enter a date (YYYY-MM-DD): ")

    try:
        # Create a Date object using the class method
        date = Date.from_string(user_input)
        # :02d formats the month and day to be two digits (ISO format)
        print(f"Valid date: {date.year}-{date.month:02d}-{date.day:02d}")
    except ValueError:  # Handle invalid date format or invalid date
        print("Invalid date or format. Please use YYYY-MM-DD.")

# ? Example Output:
# Enter a date (YYYY-MM-DD): 2026-03-08
# Valid date: 2026-03-08

# Enter a date (YYYY-MM-DD): 2024-02-35
# Invalid date or format. Please use YYYY-MM-DD.

# Enter a date (YYYY-MM-DD): abc
# Invalid date or format. Please use YYYY-MM-DD.
