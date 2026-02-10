"""Number Guessing Game Exercise"""
import random # import random module for generating random numbers

def number_guessing_game():
    """Plays a number guessing game with the user."""
    number_to_guess = random.randint(1, 100) # random number between 1 and 100
    # (using randrange would be 1-99)
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    attempts = 0 # count of attempts made by the user
    while True: # infinite loop until the correct guess
        user_input = input("Enter your guess (or type 'exit' to quit): ")
        if user_input.lower() == 'exit': # user wants to exit
            print(f"The number was {number_to_guess}. Thanks for playing!")
            break
        try: # handle wrong guess
            guess = int(user_input) # convert input to integer
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError: # handle non-integer input
            print("Invalid input. Please enter a number between 1 and 100 or 'exit' to quit.")

number_guessing_game() # start the game

# Example Output:
# Welcome to the Number Guessing Game!
# I have selected a number between 1 and 100. Can you guess it?
# Enter your guess (or type 'exit' to quit): 50
# Too high! Try again.
# Enter your guess (or type 'exit' to quit): 25
# Too low! Try again.
# Enter your guess (or type 'exit' to quit): 35
# Too high! Try again.
# Enter your guess (or type 'exit' to quit): 30
# Too high! Try again.
# Enter your guess (or type 'exit' to quit): 28
# Too low! Try again.
# Enter your guess (or type 'exit' to quit): 29
# Congratulations! You've guessed the number 29 in 6 attempts.
