# Practice — Custom Objects

This folder contains exercises, lab work, and assignments for the Custom Objects Python module.

---

## Exercises

1. Simple Object Creation
    - Scenario: Create a `Student` class with attributes `name`, `age`, and `student_id`. Add a method `study(subject)` that prints a message. Create three instances of the class.

2. Object Interaction
    - Scenario: Create a `Course` class with attributes `course_name` and a list of students. Add a method `add_student(student_object)` that adds a student instance to the list. Create a `Student` object and a `Course` object and demonstrate the interaction.

3. Inheritance and Super()
    - Scenario: Create a base class `Animal` with a method `make_sound()`. Create subclasses `Dog` and `Cat` that override `make_sound()`. Create a `SuperDog` class that inherits from `Dog` and uses `super()` to call the parent's `make_sound()` before adding its own unique sound.

4. Multiple Inheritance & MRO
    - Scenario: Create a `Writer` class with a `write()` method and a `Programmer` class with a `code()` method. Create a `TechnicalWriter` class that inherits from both `Writer` and `Programmer`. Create an instance of `TechnicalWriter` and call both `write()` and `code()`. Use `__mro__` to explain the method resolution order.

5. Class and Static Methods
    - Scenario: Create a `Date` class. Add a static method `is_valid_date(day, month, year)` that checks if a date is valid. Add a class method `from_string(date_string)` that takes a string like "2023-10-27" and creates a `Date` object.

6. Real-World Interaction
    - Scenario: Build a simple game where a `Player` object with health and damage interacts with a `Monster` object with similar attributes. Implement methods for `attack()` and `take_damage()` in both classes. The `attack()` method of one object should call the `take_damage()` method of the other.

7. Mixin Application
    - Scenario: Create a `DatabaseStorable` mixin with `save_to_db()` and `load_from_db()` methods (which just print a message for this exercise). Create a `User` class and a `Product` class. Create `StorableUser` and `StorableProduct` classes that inherit from their respective base classes and the `DatabaseStorable` mixin.

8. Complex Hierarchy
    - Design a vehicle system with `Vehicle` as a base class. Create subclasses `Car` and `Boat`. Create a `AmphibiousVehicle` class that uses multiple inheritance from both `Car` and `Boat`. Demonstrate how this class can be used both on land and in water by calling methods inherited from both parents. Use `super()`

9. Data Processing
    - Scenario: Write a Python script that reads a CSV file containing name, id, and salary for employees. Use a class method on an `Employee` class to create an `Employee` object for each row of the CSV.

10. State Management
    - Scenario: Design a class `TrafficLight` with attributes `color` and `duration`. Add a method `change_color()` that cycles through the colors (Red, Yellow, Green) and resets the duration. Use a class variable to keep track of the total number of color changes across all instances.

## Lab Work

**Individual Lab**: Create a class hierarchy for a simple inventory system.

Steps:

1. Create a base class `Product` with attributes `name`, `price`, and `quantity`.
2. Create a `Book` subclass inheriting from `Product` with `author` and `isbn`.
3. Create an `Electronics` subclass with `brand` and `warranty_months`.
4. Use `super()` in the subclasses' `__init__`
5. Create a static method in `Product` to check if a quantity value is a positive integer.
6. Create a class method in `Book` to create a new `Book` instance from a dictionary.

**Team Lab**: Build a small e-commerce simulation.
Steps:

1. Expand on the individual lab by creating a `ShoppingCart`
2. The `ShoppingCart` should be able to hold a list of `Product`
3. Implement methods to `add_item(product, quantity)`, `remove_item(product)`, and `calculate_total()`.
4. The `calculate_total()` method should be able to work with any type of `Product` object added to the cart, demonstrating polymorphism.
5. Use a mixin `Discountable` that provides a `apply_discount(percentage)` method, and apply it to a new subclass `SaleBook`.
6. Implement a `LoyaltyProgram` class that interacts with the `ShoppingCart` to apply a special discount.


## Assignment

- Task: Build a command-line-based Library management system.
- Scenario: A small library needs a system to manage books and members.
- Requirements:
1. Create a `LibraryItem` base class with attributes like `title`, `author`, and `is_checked_out`.
2. Create subclasses `Book` and `Magazine` that inherit from `LibraryItem`, with specific attributes like `isbn` for `Book` and `issue_number` for `Magazine`.
3. Create a `Member` class with `name` and `member_id`.
4. Create a `Library` class that contains lists of `LibraryItem` and `Member`.
5. Implement methods in the `Library` class to add/remove items and members, and to check out/return items. These methods should interact with the `LibraryItem` and `Member`.
6. Use a class method in `Member` to create a new member from a string of data.
7. Use a static method in `Library` to validate a member ID format.