# Practice — Functions and Scope

This folder contains exercises, lab work, assignments, and short answer questions for the Functions and Scope Python module.

---

## Exercises

1. Write a function `calculate_area(width, height)` that takes two numbers and returns the area of a rectangle.

2. Write a function `is_prime(number)` that takes an integer and returns True if it's a prime number, and False otherwise.

3. Create a module named `py`. Inside it, create a function `reverse_string(s)` and another function `count_vowels(s)`. Create a separate `main.py` file that imports and uses these functions.

4. Draw a diagram showing the scope of variables in the following code:
```Python
x = 10 # global
def my_func(y): # y is local
z = 5 # z is local
return x + y + z
```


## Lab Work

**Individual Lab**: Create a `py module` with functions to convert temperatures (Celsius to Fahrenheit and vice versa) and distances (miles to kilometers and vice versa). Create a `main.py` that acts as a user-facing menu, importing and using your converter functions based on user input.

**Team Lab**: Refactor the "Shopping Cart" lab from a previous topic. The team must move all the cart-related logic (add item, calculate total, apply discount) into functions within a py module. The main script should now be much cleaner, simply importing and calling these functions to run the checkout process.



## Assignment

Create a simple package for basic statistical calculations. The structure should be:

stats_pack/

├── __init__.py

└── calculations.py

In calculations.py, create the following functions:

- find_mean(data_list): Calculates the average.
- find_median(data_list): Finds the median value. (Hint: you'll need to sort the list).
- find_mode(data_list): Finds the most frequently occurring number.

Create a `main.py` outside this package that imports your `stats_pack` and uses the functions on a sample list of numbers.



## Short Answer Test

1. What is the purpose of the `return` statement in a function? What happens if a function does not have a `return` statement?

2. Explain the difference between a `module` and a `package` in Python.

3. Why is it generally considered bad practice to modify `global` variables from within a function?
