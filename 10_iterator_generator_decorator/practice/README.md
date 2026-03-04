# Practice — Iterators, Generators, and Decorators

This folder contains exercises, lab work, assignments, and simulated scenarios for the Iterators, Generators, and Decorators Python module.

---

## Exercises

1. Simple Iterator: Create an iterator class that produces all the even numbers up to a given limit.
    - Scenario: You need to write a class that generates a sequence of even numbers for a data processing script. The class should take a single integer, `n`, and provide numbers from 0 up to `n` (inclusive) that are even.

2. Generator with a Condition: Write a generator function that takes a list of numbers and yields only the prime numbers.
    - Scenario: You have a large list of numbers and need to efficiently filter out all the non-prime numbers for an analysis. Using a generator is crucial to avoid creating a large intermediate list.

3. Decorator with Arguments: Create a decorator that accepts an argument for a user role (e.g., 'admin', 'user'). The decorator should check if the user has the required role before executing the decorated function.
    - Scenario: In a web application, different users have different access levels. You need a simple way to protect certain functions (e.g., `delete_user`, `view_analytics`) so that only users with the 'admin' role can access them.

4. Combined Challenge: Implement a generator that processes log lines from a file (simulated). The generator should yield only the lines that contain a specific `keyword`. Then, apply a decorator to the generator that times how long it takes to process the entire log and returns the count of lines found.
    - Scenario: You are a systems administrator troubleshooting an issue from a huge log file. You need to find all instances of a specific error message and know how long the search takes.

## Lab Work

**Individual Labs**:

1. Iterators and iterables:
    - Students will create a custom class, `Sentence`, which takes a string and allows iteration over its words.
    - Objective: The class should be iterable, returning one word at a time.
    - Instructions:
        1. Create a `Sentence` class that takes a string in its `__init__`.
        2. Implement the `__iter__` method to return an iterator.
        3. Implement the `__next__` method to return the next word. Words are separated by spaces.
        4. Handle the `StopIteration` exception correctly.
    - Example Usage: `s = Sentence("This is a sample sentence"); for word in s: print(word)`

2. Generators:
    - Students will create a generator that processes a stream of data.
    - Objective: Create a generator function that reads lines from a hypothetical file (simulated by a list of strings) and yields each line, but only if it is not a comment line (starts with '#').
    - Instructions:
        1. Define a generator `process_file_lines(lines)`.
        2. Loop through the lines.
        3. Use `yield` to return a line only if it doesn't start with '#'.
        4. Test the generator with a sample list of strings.

3. Decorators:
    - Students will implement a custom `debug_logger`
    - Objective: Create a decorator that logs the function name and its arguments every time it is called.
    - Instructions:
        1. Define a decorator `debug_logger(func)`.
        2. Inside, define a `wrapper(*args, **kwargs)`.
        3. Print the function's name and its arguments using `__name__` and the `args` and `kwargs`.
        4. Call and return `func(*args, **kwargs)`.
        5. Apply the decorator to a simple function that adds two numbers.

**Team Labs**:

1. Iterators and iterables: 
    - Students will work in groups of 2-3 to debug a broken iterator code snippet provided by the instructor. The code will have common mistakes, such as not raising `StopIteration` or not returning `self` from `__iter__`.

2. Generators:
    - Students will work in groups to implement a simple "echo" generator that takes input via `send()` and yields it back, but with some modification.
    - Objective: The generator should take a number, multiply it by a factor (e.g., 2), and yield the result. The factor itself should be modifiable by a subsequent `send()`.
    - Instructions:
        1. Define a generator `transformer()`.
        2. The generator should have a loop that accepts input via `yield` and multiplies it by a pre-set factor, then prints the result.
        3. The loop should also be able to receive a new factor via `send()`.
    - Example Usage: `gen = transformer(); next(gen); gen.send(5); gen.send(3); gen.send(10)`

3. Decorators:
    - Students will work in groups to create a decorator that caches the results of a function call.
    - Objective: Implement a `memoize` decorator that stores the return values of a function based on its arguments. If the function is called with the same arguments again, it returns the cached result instead of re-executing.
    - Instructions:
        1. Define a decorator `memoize`.
        2. Inside the wrapper, use a dictionary to store the cache. The key should be a tuple of the arguments.
        3. Check if the arguments are in the cache. If so, return the cached value.
        4. If not, call the function, store the result in the cache, and return it.
        5. Apply the decorator to a slow, recursive function (e.g., a Fibonacci sequence calculation) to demonstrate the performance gain.


## Assignments

1. Iterators and iterables:

You are given a dictionary where keys are student names and values are a list of their grades. Create an iterable class `StudentGrades` that takes this dictionary. When you iterate over an instance of this class, it should yield the student's name, their average grade, and a status of 'Pass' (average >= 70) or 'Fail' (average < 70).

2. Generators:

Your company wants to analyze a large log file. Write a generator function that takes a file path as input and yields each line of the file. Then, create a second generator that takes the first generator as input and yields only those lines that contain the keyword `"ERROR"`. Finally, create a third function that uses a for loop to print the first 10 error lines found.

3. Decorators:

Create a decorator that validates the arguments passed to a function. The decorator should take min_val and max_val arguments. If any of the arguments passed to the decorated function are outside this range, the decorator should raise a ValueError. The decorator should work for any function that takes a variable number of numeric arguments.

## Simulated Scenarios

1. Large Dataset Processing

- Problem Case: A startup is working on a recommendation engine. They have a 5GB CSV file of user interactions, and they need to find the top 100 most frequent item IDs. Loading the entire file into memory is impossible due to resource constraints.
- Analysis and Understanding: The problem requires processing a massive file without loading it all into memory. This is a classic use case for generators. A generator can be used to read the file line by line, process each line, and then update a frequency counter. This approach uses constant memory regardless of the file size.
- Resolution:
    1. Create a generator function `read_file_by_line(file_path)` that opens the file and yields each line.
    2. Create a second generator `process_item_ids(lines_generator)` that takes the first generator as input, parses each line to extract the item ID, and yields the ID.
    3. In the main script, iterate over the `process_item_ids` generator. Use a dictionary to count the frequency of each item ID.
    4. After the iteration is complete, sort the dictionary items by frequency and print the top 100.
 

2. API Rate Limiting

- Problem Case: You are integrating with a third-party API that has a strict rate limit of 5 requests per second. Your application makes hundreds of calls, and without proper management, it will get blocked.
- Analysis and Understanding: This problem requires managing the execution rate of a function. A decorator is the perfect solution. The decorator can be applied to any function that makes an API call. It can then manage the timing, ensuring that calls are spaced out and do not exceed the rate limit.
- Resolution:
    1. Create a `rate_limit_decorator` that takes the maximum number of calls and a time interval as arguments.
    2. The decorator's wrapper function should keep track of the timestamps of recent calls.
    3. Before calling the decorated function, the wrapper should check if a new call would violate the rate limit. If so, it should use `sleep()` to wait for the required duration.
    4. Apply this decorator to all functions that interact with the third-party API.
 

3. Real-Time Scenario: User Authentication and Authorization

- Requirement: Your team is building a content management system. You need to ensure that only logged-in users can access certain pages and that only users with 'editor' or 'admin' roles can create or delete content. You must implement this with minimal changes to the existing view functions.
- Guidelines to Follow:
    - Single Responsibility Principle: Don't mix authentication logic with your core business logic (e.g., creating a post).
    - Reusability: The authentication check should be reusable across multiple view functions.
- Steps to Resolve:
    1. Create a decorator `login_required` that checks if a user is authenticated. If not, it should redirect them to the login page.
    2. Create a second decorator `role_required(roles)` that takes a list of allowed roles. The decorator will check if the user's role is in the allowed list. If not, it will return an access denied message.
    3. Apply `@login_required` to all view functions that require a user to be logged in.
    4. Apply `@role_required(['editor', 'admin'])` to view functions that require specific permissions, ensuring it is placed inside the `@login_required`