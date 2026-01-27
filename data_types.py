"""Core Data Types"""

# Integer (int)
X = 5
print(type(X))  # <class 'int'>

# Floating point numbers (float)
Y = 3.14
print(type(Y))  # <class 'float'>

# String (str)
Z = "Hello, World!"
print(type(Z))  # <class 'str'>

# Boolean (bool)
A = True
print(type(A))  # <class 'bool'>

# Reassign the variable data type and point to it
Y = 'new data'
print(type(Y))  # <class 'str'>
Y = 8.9
print(type(Y))  # <class 'float'>

# Immutable Data Types - str, int, float, tuple, range, bool

# Strings:
print("Immutable data types:")
print("Strings:")
NAME = "Anton"
print(type(NAME))  # <class 'str'>
print(id(NAME))  # 2206725132704

NAME = NAME.upper()
# A new string is created in memory and reassigns the variable name to point to it
print(NAME)
print(type(NAME))  # <class 'str'>
print(id(NAME))  # 2206725133568
# A new ID is assigned to the string, displaying how strings are immutable

# Strings with operators:
D = "Data"
print(D)  # Data
print(id(D))  # 1981393098368
S = "Science"
print(id(S))  # 1981393098656
D = D + S
print(D)  # DataScience
print(type(D))  # <class 'str'>
print(id(D))  # 1981393140848 - new ID assigned
print(id(S))  # 1981393098656 - original ID
print(S)  # Science - original string
# D is reassigned, S did not change

# Integers:
print("Integers:")
X = 6
print(type(X))  # <class 'int'>
print(id(X))  # 140707501995288
X = 5
print(type(X))  # <class 'int'>
print(id(X))  # 140707501995256 - new ID assigned

# Floats:
print("Floats:")
X = 6.5
print(type(X))  # <class 'float'>
print(id(X))  # 2285426285488
X = 5.3
print(type(X))  # <class 'float'>
print(id(X))  # 2285426285648 - new ID assigned

# Tuples:
print("Tuples:")
points = ()
print(type(points))  # <class 'tuple'>
print(id(points))  # 140707502071512
points = (1, 2, 3, 4, 5)
print(type(points))  # <class 'tuple'>
print(id(points))  # 1596275363936 - new ID assigned

# Ranges:
print("Ranges:")
numbers = range(1, 10)
print(type(numbers))  # <class 'range'>
print(numbers)  # range(1, 10)
print(id(numbers))  # 2551408489936
for i in range(5):
    print("Printing range upto 5: ", i)  # 0, 1, 2, 3, 4
for i in range(2, 8):
    print("Printing range from 2 to 8: ", i)  # 2, 3, 4, 5, 6, 7
for i in range(1, 10, 2):
    print("Printing range from 1 to 10 with step 2", i)  # 1, 3, 5, 7, 9
numbers = range(1, 20)
print(id(numbers))  # 2551409042720 - new ID assigned

# Booleans:
print("Booleans:")
X = True
print(type(X))  # <class 'bool'>
print(id(X))  # 140707501099776
X = False
print(type(X))  # <class 'bool'>
print(id(X))  # 140707501099808 - new ID assigned

# Mutable Data Types - lists, disctionaries, sets

# Lists:
print("Lists:")
random_list = []  # Defines empty list
print(type(random_list))  # <class 'list'>
print(id(random_list))  # 1377744762624
random_list = [1, 2, 3, "data", 10.5, True]  # Defines new list
print(type(random_list))  # <class 'list'>
print(id(random_list))  # 1377744646016 - new ID assigned = immutable
print(random_list)  # [1, 2, 3, 'data', 10.5, True]
random_list.append(33)  # Add 33 to list, same list but appended
print(len(random_list))  # 7 (length)
print(id(random_list))  # 1377744646016 - append did not change ID = mutable

# Sidenote - Assignment vs. Object Duplication:
print("Assignment:")
A = [1, 2, 3]
print(id(A))  # 2161826094528
B = []
print(id(B))  # 2161825721280
B = A
print(id(A))  # 2161826094528
print(id(B))  # 2161826094528 - assignment points both variables to same object
B.append(4)
print(A)  # [1, 2, 3, 4] - appends to A as well as B
print(B)  # [1, 2, 3, 4]
print(id(A))  # 2161826094528
print(id(B))  # 2161826094528 - same ID = mutable

print("Object Duplication:")
X = [1, 2, 3]
Y = X.copy()
print(id(X))  # 2058328648640
print(id(Y))  # 2058328819456 - duplication assigns new ID
Y.append(4)
print(X)  # [1, 2, 3]
print(Y)  # [1, 2, 3, 4] - appended after duplication
print(id(X))  # 2058328648640 - same ID
print(id(Y))  # 2058328819456 - same ID


# Dictionaries:
print("Dictionaries:")
person = {}
print(type(person))  # <class 'dict'>
print(id(person))  # 1930366867456
person = {"name": "Anton", "age": 31, "address": "UK", "score": 80.5}
print(type(person))  # <class 'dict'>
print(id(person))  # 1930366869184 - new ID assigned
print(person)  # {'name': 'Anton', 'age': 31, 'address': 'UK', 'score': 80.5}
print(person["name"])  # Anton
person["email"] = "newemail@gmail.com"
print(person)
# {'name': 'Anton', 'age': 31, 'address': 'UK', 'score': 80.5, 'email': 'newemail@gmail.com'}
print(id(person))  # 1930366869184
# Same ID after adding new 'key: value' pair = mutable

# Sets:
print("Sets:")
S = set()
print(type(S))  # <class 'set'>
print(id(S))  # 2241781090560
S = {1, 2, 3, 4, 5, 5, 5, 'data', 10.4, True}  # True bool = 1
print(type(S))  # <class 'set'>
print(id(S))  # 2241781440896 - new ID assigned
print(S)  # {1, 2, 3, 4, 5, 10.4, 'data'}
# Sets remove duplicate entries (5, 5, True)
print(len(S))  # 7 = duplicate entries not counted
print("data" in S)  # True = this exists in the Set

# Sidenote - Operators
A = {100, 200, 300}
B = {300, 400, 500}
print(A)  # {200, 100, 300}
print(B)  # {400, 300, 500}
print(A | B)
# {400, 100, 500, 200, 300} - combines elements without duplicates
print(A & B)  # {300} - displays common elements in both sets
print(A - B)  # {200, 100} - elements in A but not in B
