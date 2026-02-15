"""Iterators, Generators, and Decorators"""

# ! ------------------------------------------------------------------------------------------------

# ! ITERATORS AND ITERABLES

# ! ------------------------------------------------------------------------------------------------

# ! Iterators are objects that can be iterated upon, so we can traverse through all the values.

# ! An iterable is an object that can return an iterator, which can be used to iterate through
# ! the values of the iterable.

l1 = [1, 2, 3, 4]
print(dir(l1))

# __iter__() is a method that returns an iterator object for the given iterable (here, the list l1).
it = l1.__iter__()

# But calling dunder methods directly is not recommended. Instead, use the built in iter() function:
it = iter(l1)

print(it)
# ? Output: <list_iterator object at 0x00000222EA2005B0>

# __next__() is a method that returns the next item from the iterator. When there are no more
# items to return, it raises a StopIteration exception.
print(it.__next__())
# ? Output: 1

# This is the correct way to create an iterator object for the list l1 using the iter() function,
# which is a built-in function that returns an iterator object for the given iterable.
it = iter(l1)
print(next(it))
# ? Output: 1

# ? How does this work internally?
# When we call iter(l1), it internally calls the __iter__() method of the list l1, which returns
# an iterator object for the list. This iterator object has a __next__() method that can be
# called to get the next item from the list. When we call next(it), it internally calls the
# __next__() method of the iterator object it, which returns the next item from the list l1.
# This process continues until there are no more items to return, at which point a
# StopIteration exception is raised.

# ? ------------------------------------------------------------------------------------------------

# ? range(1, 100) is an iterable that returns an iterator object when we call iter() on it.
# ? We can use this iterator object to iterate through the range values using next().

# ? Range object stores:
start = 1
stop = 100
step = 1  # step is an interval between the numbers in the range (1 by default)

# ? Heap memory:
# ? range(1, 100) only stores start/stop/step

# Heap memory is a region of memory that is used for dynamic memory allocation.
# When we create an object in Python, it is stored in the heap memory.

# In heap memory, the range object only stores the start, stop, and step values, and it does not
# store all the values from 1 to 99. When we call next() on the iterator object of the range,
# it calculates the next value based on the start, stop, and step values and returns it.

# This is why range is an efficient way to generate a sequence of numbers without storing them
# all in memory at once.


# ? Stack memory:
# ? A list like list(range(1, 100)) would store all the values.
# Stack memory is a region of memory that is used for static memory allocation. When we call a
# function in Python, a new frame is created in the stack memory to store the local variables.

# ? Range in stack memory would store all the values from 1 to 99, taking up a lot of memory:
# i = 1
# i = 2
# i = 3
# i = ...
# i = 99
# ? Note that this is not how range actually works, but if it did store all the values in
# ? stack memory, it would take up a lot of memory and be inefficient.

# ? ------------------------------------------------------------------------------------------------

# ? for loops in Python are designed to work with iterables.
# When we use a for loop to iterate over an iterable, Python internally creates an iterator object
# for that iterable and uses it to get the next item in each iteration of the loop.

data = [1, 2, 3, 4, 5, 6]  # iterable (a list in this case)

for i in data:
    print(i)

# ? Output:
# ? 1
# ? 2
# ? 3
# ? 4
# ? 5
# ? 6


# ? Internally:
data = [1, 2, 3, 4, 5, 6]  # iterable

# This creates an iterator object for the list data using the iter() function,
# which internally calls the __iter__() method of the list to get the iterator.
it = iter(data)  # `it` is reset from the previous example

print(it)
# ? Output: <list_iterator object at 0x00000222EA2005B0>

# ? ------------------------------------------------------------------------------------------------

# ? while loops can also be used to iterate through an iterable.
# They use next() to get the next item from the iterator until a StopIteration exception is raised.

while True:
    try:
        # This will call the __next__() method of the iterator object `it`
        i = next(it)
        print(i)
    # Catch the StopIteration exception raised when there are no items to return.
    except StopIteration:
        break

# ? Output:
# ? 1
# ? 2
# ? 3
# ? 4
# ? 5
# ? 6

# ? ------------------------------------------------------------------------------------------------

# ? Example: Creating a custom iterator by defining a class with __iter__() and __next__() methods.


class Playlist:
    def __init__(self, songs):  # list of songs
        self.songs = songs
        self.index = 0

    def __iter__(self):  # Called when creating an iterator object for Playlist class using iter()
        return self

    def __next__(self):  # Called when we call next() on the iterator object of the Playlist class
        if self.index < len(self.songs):  # Check if there are more songs to return
            # Get the current song based on the index
            song = self.songs[self.index]
            self.index += 1  # Increment the index for the next call to __next__()
            return song
        raise StopIteration  # Raise StopIteration when there are no more songs to return


p1 = Playlist(["song1", "song2", "song3"])

for song in p1:
    print(song)

# ? Output:
# ? song1
# ? song2
# ? song3

# ! ------------------------------------------------------------------------------------------------

# ! GENERATORS

# ! ------------------------------------------------------------------------------------------------

# ? Generators are a special type of iterators that allow us to create iterators in a more concise
# ? and efficient way. They are defined using a function with the `yield` keyword (not return).
# ? When a generator function is called, it returns a generator object that can be iterated over.
# ? Yield statement is used to produce a value and pause the execution of the generator function,
# ? allowing it to resume from the same point when the next value is requested.

# ? Generators are useful for generating a sequence of values quickly without having to store the
# ? entire sequence in memory, beneficial when working with large datasets or infinite sequences.

# ? Generator function:


def gen1():
    yield 1
    yield 2
    yield 3
    yield 4


g1 = gen1()

print(g1)
# ? Output: <generator object gen1 at 0x00000222EA2005B0>

print(next(g1))  # ? Output: 1
print(next(g1))  # ? Output: 2
print(next(g1))  # ? Output: 3
print(next(g1))  # ? Output: 4
# print(next(g1))  # This will give an error because there are no more values to yield.

for i in gen1():
    print(i)

# ? Output:
# ? 1
# ? 2
# ? 3
# ? 4

# ? Comapring generators and lists:


def squared(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result


data = squared(100000)

# ? What happens internally here?
# The result list creates an empty list in memory, then it iterates through the range
# of 100000 squares and appends the square of each number to the list. This can consume
# a lot of memory (RAM) if n is large.

# ? Using a generator instead:


def squared_gen(n):
    for i in range(n):
        yield i * i


data_gen = squared_gen(100000)

# ? What happens internally here?
# When we call squared_gen(100000), it returns a generator object that can be iterated
# over. The generator function does not create a list in memory; instead, it generates
# each square value spontaneously as we iterate through it. This is much more memory-efficient,
# especially for large values of n, as it does not store all the squared values in memory at once.

# ? Steps:
# - It creates a generator object
# - Generates one square
# - Returns the square and pauses
# - The value is consumed (e.g., printed or stored in a variable)
# - Discards the generated value from memory
# - Generates the next square

# Only one square value is in memory at any given time, so it's more efficient for large datasets.

# ? Executing this can lead to a crash/freeze:
# l1 = [x * x for x in range(10000000000000000000000000)]
# print(l1)
# This will give a MemoryError because it tries to create a list of squares for a very large range,
# which exceeds the available memory.

# ? After first execution write this:
# l1 = (x * x for x in range(10000000000000000000000000))
# print(l1)
# This will not give a MemoryError because it creates a generator expression instead of a list,
# which generates each square value on-the-fly without storing them all in memory at once.

# while True:
# print(next(l1))
# This will keep generating and printing square values indefinitely until we stop the execution,
# demonstrating the memory efficiency of generators even for very large or infinite sequences.

# ? Output:
# 0
# 1
# 4
# 9
# 16
# ... (continues indefinitely)


# ! ------------------------------------------------------------------------------------------------

# ! DECORATORS

# ! ------------------------------------------------------------------------------------------------

# ? Decorators are a way to add extra functionality to a function or method without changing its
# ? original code. They are defined as functions that take another function as an argument and
# ? return a new function that has the additional functionality added to it.

def str_upper(func):
    def inner():
        s1 = func()  # This will call the original function and get its return value
        return s1.upper()  # This will convert the return value to uppercase and return it
    return inner  # This will return the inner function that has the extra functionality added to it


@str_upper  # This is a decorator that applies the str_upper function to the greet function
def greet():
    return "good morning"
# ? Output: GOOD MORNING


# Call the wrapped function greet, which has been decorated with str_upper.
print(greet())  # ? Output: GOOD MORNING

# Shows the inner function that is returned by the decorator.
print(greet)
# ? Output: <function str_upper.<locals>.inner at 0x0000019F7A178040>
