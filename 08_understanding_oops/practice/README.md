# Practice — Files and I/O

This folder contains lab work and an assignment for the Files and I/O Python module.

---

## Lab Work

**Individual Lab**: 

- Task: Create a class hierarchy for geometric shapes.
- Steps:
  1. Create a base class `Shape` with a method `area()` that raises a `NotImplementedError`.
  2. Create subclasses `Circle` and `Rectangle` that inherit from `Shape`.
  3. Implement the `__init__` method for each subclass to take appropriate parameters (radius for `Circle`, width and height for `Rectangle`).
  4. Override the `area()` method in each subclass to calculate and return the correct area.
  5. Create instances of both `Circle` and `Rectangle` and call the `area()` method to test.
  6. Create a function `calculate_total_area(shapes)` that takes a list of `Shape` objects and calculates the sum of their areas, demonstrating polymorphism.

**Team Lab**: 

- Task: Build a simple student management system using inheritance.
- Steps:
  1. Start with a `Person` base class with `name` and `age`.
  2. Create a `Student` class inheriting from `Person` with additional attributes `student_id` and `courses`.
  3. Create a `Teacher` class inheriting from `Person` with `employee_id` and `subjects`.
  4. Use `super().__init__()` correctly in both `Student` and `Teacher` to call the parent class's constructor.
  5. Create a `Course` class that has `course_name` and lists for `students` and `teachers`.
  6. Implement a class method in the `Student` class that acts as an alternative constructor to create a `Student` from a dictionary.
  7. Implement a static method in the `Course` class that checks if a student ID is in a valid format.
  8. Demonstrate encapsulation by using a double underscore for the `__student_id` attribute in the `Student`


## Assignment

- Task: Design and implement a simple Vehicle rental system.
- Scenario: A company rents out different types of vehicles.
- Requirements:
  1. Create a base class `Vehicle` with attributes `make`, `model`, `year`, and a method `display_info()`.
  2. Create subclasses `Car`, `Motorcycle`, and `Truck` that inherit from `Vehicle`.
  3. Add specific attributes to each subclass (e.g., `num_doors` for `Car`, `engine_type` for `Motorcycle`).
  4. Override the `display_info()` method in each subclass to provide more specific information.
  5. Use multiple inheritance to create a `HybridCar` class that inherits from `Car` and a new `ElectricVehicle` mixin class. The `ElectricVehicle` mixin should provide an `electric_info()`.
  6. The `HybridCar` class should implement both `display_info()` and `electric_info()` and correctly use `super()`.