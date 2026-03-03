# Practice — Files and I/O

This folder contains exercises, lab work, and assignments for the Files and I/O Python module.

## Exercises

1. **Exercise 1: Simple Text File Logger**

   Write a Python script that asks the user for a single line of text. The script should then append this line, along with a timestamp, to a file named `log.txt`. The script should not overwrite the file if it already exists.

2. **Exercise 2: Student Grade Calculator**

   You have a text file named `grades.txt` where each line contains a student's name followed by their score, separated by a comma (e.g., `John Doe,85`). Write a program that reads this file, calculates the average score of all students, and then writes the result to a new file called `average_grade.txt` in a human-readable format.

3. **Exercise 3: Inventory Management System**

   Create a program that manages a small inventory. The inventory data should be stored in a JSON file named `inventory.json`. The program should have functions to:

   - Load the inventory from the file.
   - Add a new item to the inventory (item name, quantity, price).
   - Update the quantity of an existing item.
   - Save the updated inventory back to the JSON file.

   The program should handle cases where the file does not exist initially.

## Lab Work

**Individual Lab: Contact Book Application**

Create a simple command-line contact book application. The application should store contact information (name, phone number, email) in a text file named `contacts.txt`. The program should have options to add a new contact, view all contacts, and search for a contact by name. Ensure all data is saved persistently.

## Assignment

Develop a Python script that processes a large log file (`server.log`).

- The script should read the log file line by line, identify all lines containing the word `"ERROR"`, and write these error lines to a new file named `errors.log`.
- Additionally, for each error, count the number of times it occurred and save this summary in a separate JSON file named `error_summary.json`.
- The script must be robust and handle potential `IOError` exceptions.