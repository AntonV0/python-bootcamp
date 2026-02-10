"""Individual Lab: Write a script to validate a password based on specific criteria"""

def validate_password(password):
    """
    Check if password has at least 8 characters, 
    one uppercase letter, one lowercase letter, and one number.
    """
    has_upper = False
    has_lower = False
    has_number = False
    has_8_characters = False

    if len(password) >= 8:
        has_8_characters = True

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_number = True

    if has_8_characters and has_upper and has_lower and has_number:
        print("Password is valid.")

    else:
        print( "Password is invalid. It must be at least 8 characters long and contain " \
               "at least one uppercase letter, one lowercase letter, and one number."
        )

user_password = input("Enter your password: ")
validate_password(user_password)

# Example usage:
# Enter your password: Test1234
# Password is valid.
# Enter your password: test
# Password is invalid. It must be at least 8 characters long and contain
# at least one uppercase letter, one lowercase letter, and one number.
