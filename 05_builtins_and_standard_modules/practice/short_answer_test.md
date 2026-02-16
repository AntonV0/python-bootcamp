## Short Answer Test - Built-ins and Standard Modules

### Q1. What is the difference between `random()` and `random.randint()`.

**Answer:**  
- `random()` returns a random floating-point number between 0.0 and 1.0 (could be 0.0 but not 1.0). 
- `random.randint()` returns a random integer between the specified range (inclusive of both endpoints). 
- For example `random.randint(1, 10)` will return an integer between 1 and 10 (including both 1 and 10).

---

### Q2. Name three built-in functions (from the builtins module) and briefly describe what they do.

**Answer:**  
- `len()`: Returns the number of items in an object (like a list, string, etc.).
- `print()`: Outputs the specified message to the console.
- `type()`: Returns the type of an object (like `int`, `str`, `list`, etc.).

---

### Q3. How would you import and use the value of Pi from the math module?

**Answer:**  
```python
import math
pi_value = math.pi
print(pi_value)
```
