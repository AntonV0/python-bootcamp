"""Flow Control in Python"""

# ! FOR LOOPS - Iterate over a sequence

num = int(input('Enter a number: '))  # Convert input to integer
print(num + 1)  # Print number plus one
# ? Example: If input is 20, output will be 21

for i in range(1, 10):
    print(f"{num} * {i} = {i * num}")  # Print multiplication table

# for i in range(1, 10):
# print(num, " * ", i , " = " ,num * i) # Alternative format

# ? Example: If input is 20, output will be:
# 20 * 1 = 20
# 20 * 2 = 40
# 20 * 3 = 60
# 20 * 4 = 80
# 20 * 5 = 100
# 20 * 6 = 120
# 20 * 7 = 140
# 20 * 8 = 160
# 20 * 9 = 180

# ? Loop through squares of numbers
for i in range(1, 6):  # Square of numbers from 1 to 5
    print(f"Square of {i} is {i**2}")  # Print square of the number
# Output:
# Square of 1 is 1
# Square of 2 is 4
# Square of 3 is 9
# Square of 4 is 16
# Square of 5 is 25

# ? Loop through a dictionary
d = {}  # Initialise empty dictionary
d['name'] = 'Anton'
d['age'] = 31
d['address'] = 'UK'
for key, value in d.items():
    print(key, ":", value)
# ? Output:
# name : Anton
# age : 31
# address : UK

# ? Loop to find prime numbers
for i in range(1, 100):  # Prime numbers between 1 and 100
    IS_PRIME = True
    for j in range(2, int(i**0.5) + 1):  # Check divisibility up to square root of i
        if i % j == 0:  # If i is divisible by j
            IS_PRIME = False
            break  # No need to check further
    if IS_PRIME and i > 1:
        print(i, end=' ')  # Print prime numbers on the same line
# ? Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

# ? Take user input 5 times and add data to empty list (FOR LOOP version)
user_list_for = []  # Initialise empty list
for _ in range(5):  # Loop 5 times
    user_input = input('Enter some data: ')  # Take user input
    user_list_for.append(user_input)  # Add input to list
print("You entered:", user_list_for)  # Print all user inputs
# ? Example: If inputs are a, b, c, d, e, output will be:
# You entered: ['a', 'b', 'c', 'd', 'e']

#  ! -------------------------------------------------------------------

# ! WHILE LOOPS - execute as long as condition is true

# ? Loop to print multiplicatio table with user confirmation to continue
num_to_multiply = int(input('Enter a number:'))
i = 1
while i <= 10:
    # Print multiplication table
    print(f"{num_to_multiply} * {i} = {num_to_multiply * i}")
    i += 1  # Increment i by 1
    break_condition = input('Do you want to continue? (yes/no): ')
    if break_condition.lower() != 'yes':
        break  # Exit loop if user does not want to continue

# ? Example: If input is 20, output will be (if condition is accepted to continue):
# 20 * 1 = 20
# Do you want to continue? (yes/no): yes (this repeats until i > 10 or user inputs no)
# 20 * 2 = 40
# 20 * 3 = 60
# 20 * 4 = 80
# 20 * 5 = 100
# 20 * 6 = 120
# 20 * 7 = 140
# 20 * 8 = 160
# 20 * 9 = 180
# 20 * 10 = 200

# ? Take user input 5 times and add data to empty list (WHILE LOOP version)
user_list_while = []  # Initialise empty list
i = 0
while i < 5:
    user_input = input('Enter some data: ')  # Take user input
    user_list_while.append(user_input)  # Add input to list
    i += 1
print("You entered:", user_list_while)  # Print all user inputs
# ? Example: If inputs are a, b, c, d, e, output will be:
# You entered: ['a', 'b', 'c', 'd', 'e']

# ? Generate prime numbers from 2 to 20
NUM = 2  # Start from 2 - the first prime number
while NUM <= 20:
    IS_PRIME = True
    for i in range(2, int(NUM**0.5) + 1):  # Check divisibility up to square root of NUM
        if NUM % i == 0:  # If NUM is divisible by i
            IS_PRIME = False
            break
    if IS_PRIME:
        print(NUM, end=' ')  # Print prime numbers on the same line
    NUM += 1  # Increment NUM by 1
# ? Output: 2 3 5 7 11 13 17 19

# ! -------------------------------------------------------------------

# ! IF/ELSE STATEMENTS - Conditional execution

# ? Check voting eligibility
age = int(input('Enter your age: '))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
# ? Example: If input is 20, output will be:
# ? Eligible to vote

# ? Check if a number is prime using IF statement
num_to_check = int(input('Enter a number to check if it is prime: '))
IS_PRIME = True
for i in range(2, num_to_check):  # Check divisibility
    if num_to_check % i == 0:  # If divisible without remainder
        IS_PRIME = False
        break
if IS_PRIME and num_to_check > 1:  # Check if number is greater than 1
    print(f"{num_to_check} is a prime number")
else:
    print(f"{num_to_check} is not a prime number")
# ? Example: If input is 7, output will be:
# ? 7 is a prime number

# ? Check if number is odd or even
val = int(input("Enter an integer: "))
for val in range(1, 51):
    if val % 2 == 0:
        print(f"{val} is even")
    else:
        print(f"{val} is odd")
# ? Output:
# 1 is odd
# 2 is even
# 3 is odd
# ...
# 50 is even

# ? Find the first prime number after 100
NUM = 101  # Start checking from 101
while True:  # Loop indefinitely
    IS_PRIME = True  # Assume NUM is prime
    for i in range(2, int(NUM**0.5) + 1):  # Check divisibility up to square root of NUM
        if NUM % i == 0:  # If NUM is divisible by i
            IS_PRIME = False
            break  # No need to check further
    if IS_PRIME:  # If NUM is prime
        print(f"The first prime number after 100 is {NUM}")
        break  # Exit loop
    NUM += 1  # Increment NUM by 1
# ? Output:
# ? The first prime number after 100 is 101

# ! -------------------------------------------------------------------

# ! Interactive Menu Exercise:

while True:
    option = int(
        input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide, 0 to exit: "))

    if option == 0:  # Exit the loop if user chooses to exit
        break
    if option in (1, 2, 3, 4):  # Check if option is valid
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == 1:
            print(num1 + num2)
        elif option == 2:
            print(num1 - num2)
        elif option == 3:
            print(num1 * num2)
        elif option == 4:
            if num2 != 0:
                print(num1 / num2)
            else:
                print("Error: Cannot divide by 0")
    else:
        print("Invalid option.")

# ? Example interaction:
# ? Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide, 0 to exit: 1
# ? Enter first number: 10
# ? Enter second number: 5
# ? 15.0
# ? Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide, 0 to exit: 0
# ? (Program exits)
