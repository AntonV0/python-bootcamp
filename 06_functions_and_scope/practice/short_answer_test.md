## Short Answer Test - Functions and Scope

### Q1. What is the purpose of the `return`statement in a function? What happens if a function does not have a `return` statement?

**Answer:**  
The `return` statement is used to exit a function and optionally pass back a value to the function caller. If a function does not have a `return` statement, it will return `None` by default when it finishes executing. So the output of the function will be `None` if you try to use its return value.

---

### Q2. Explain the difference between a `module` and a `package` in Python.

**Answer:**  
A `module` is a single Python file that contains functions, classes, or variables that can be imported and used in other Python code. A `package` is a collection of modules organised in a directory hierarchy, typically containing an `__init__.py` file, which allows the directory to be treated as a package. A package can contain multiple modules and sub-packages, allowing for better organisation of code.

---

### Q3. Why is it generally considered bad practice to modify `global` variables from within a function?

**Answer:**  
Modifying `global` variables from within a function can lead to code that is difficult to understand and maintain. Functions that rely on or change global state can produce side effects that are hard to track, making debugging more difficult. It is usually better to pass variables as parameters and return new values, keeping functions self-contained.
