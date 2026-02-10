# Practice — Core Data Types & Data Structures

This folder contains exercises, lab work, assignments, and short answer questions for the Core Data Types Python module.

---

## Exercises

1. Create a script that takes a sentence as input and uses a dictionary to count the frequency of each word. The output should be the word and its count.

2. Write a program that manages a to-do list. Use a list of dictionaries, where each dictionary represents a task with a 'description' (string) and a 'completed' (boolean) key. Implement functions to add a task, mark a task as complete, and view all tasks.

You are given two lists of student IDs, one for students enrolled in Math and one for students in Science. Write a script that uses sets to find:  
(a) Students enrolled in both courses.  
(b) All unique students enrolled in either course.  
(c) Students enrolled in Math but not Science.

4. Draw a diagram that represents the user dictionary:  
`user = {'id': 101, 'name': 'Alice', 'roles': ['editor', 'viewer']}`  
in memory. Show how the variables user, id, name, and roles point to their respective data objects.

---

## Lab Work

**Individual Lab**: Create a "Contact Book" program. The main data structure should be a dictionary where keys are contact names and values are another dictionary containing their phone number and email. The program should allow the user to add, look up, and delete contacts.

**Team Lab**: Extend the Contact Book. The team must implement a feature to save the contact dictionary to a file using `json.dump()` and load it back when the program starts using `json.load()`. They must also add data validation to ensure the phone number contains only digits and the email contains an @ symbol.

---

## Assignment

Create a script `inventory.py`. The inventory should be a list of dictionaries. Each dictionary represents a product with keys 'product_id', 'name', 'price', and 'stock'.

Populate the inventory with at least 4 products.  
Write a function that calculates the total value of all items in stock (price * stock for each item, summed up).  
Write a function that finds and returns the product with the highest price.  
Print the results in a well-formatted way.

---

## Short Answer Test

Explain the concept of mutability and provide a code example that demonstrates a common bug related to modifying a mutable object that is referenced by multiple variables.

Describe a real-world scenario where a dictionary is a more appropriate data structure than a list. Justify your choice.

What are the key differences between a set and a list? When would you choose to use a set?
