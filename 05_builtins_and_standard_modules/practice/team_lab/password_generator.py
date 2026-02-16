"""Password Generator using random module"""

import random  # To use choice() and random.shuffle() functions

# ? Lists of characters to use in password generation:
lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']


def generate_password(length):
    """Generate a random password of a given length."""

    password_characters = []  # Initialise empty list

    if length < 8 or length > 20:
        return None  # Invalid length

    # ? Ensure the password includes at least one character from each category
    password_characters.append(random.choice(lowercase_list))
    password_characters.append(random.choice(uppercase_list))
    password_characters.append(random.choice(digits_list))
    password_characters.append(random.choice(special_characters_list))

    # ? Fill the remaining length with random choices from all categories combined
    all_characters = (lowercase_list + uppercase_list + digits_list +
                      special_characters_list)  # Combine all character lists into one
    for _ in range(length - 4):  # Subtract 4 to account for the characters already added
        password_characters.append(random.choice(all_characters))

    # ? Shuffle the list to ensure randomness and then join to form the final password string
    random.shuffle(password_characters)
    return ''.join(password_characters)


# ? Loop to allow multiple attempts at generating a password until valid input is provided
while True:
    try:
        password_length = int(
            input("Enter the desired password length (8-20): "))

        # ? Generate password using the function defined above
        password = generate_password(password_length)

        if password is None:  # Check if the password generation failed due to invalid length
            print("Invalid length. Please enter a number between 8 and 20.")
            continue  # Prompt the user again if the length was invalid

        print("Generated Password:", password)
        break  # Exit the loop after successfully generating a password

    except ValueError:  # Catch the case where the user input cannot be converted to an integer
        print("Invalid input. Please enter a valid integer for the password length.")

# ? Example output:

# ? Enter the desired password length (8-20): 12
# ? Generated Password: PA68Bn^*cvWz

# ? Enter the desired password length (8-20): 5
# ? Invalid length. Please enter a number between 8 and 20.

# ? Enter the desired password length (8-20): 25
# ? Invalid length. Please enter a number between 8 and 20.

# ? Enter the desired password length (8-20): abc
# ? Invalid input. Please enter a valid integer for the password length.
