"""Exercise 9: Data Processing"""

from pathlib import Path


class Employee:
    """Employee class with attributes for name, employee ID, and salary."""

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    @classmethod
    def from_csv_row(cls, row):
        """Create an Employee object from a CSV row."""
        name, employee_id, salary = row.split(",")
        return cls(name, int(employee_id), int(salary))

    def __str__(self):  # Define the string representation of the object for better output
        return f"Employee(ID: {self.employee_id}, Name: {self.name}, Salary: £{self.salary})"


if __name__ == "__main__":
    # Construct the file path to the CSV file
    file_path = Path(__file__).parent / "09_data_processing.csv"

    # Read the CSV file and create Employee objects
    with file_path.open("r", encoding="utf-8") as file:
        data = file.read()
    # read line by line and split where there is a comma
    lines = data.strip().split("\n")[1:]  # Skip the header line
    employees = []  # List to hold Employee objects
    for line in lines:
        # Create an Employee object using the class method and add it to the list
        employee = Employee.from_csv_row(line)
        employees.append(employee)
    for emp in employees:
        print(emp)  # Print the Employee objects

# ? Contents of 09_data_processing.csv:
# name,id,salary
# Alice,1,50000
# Bob,2,62000
# Charlie,3,58000
# Dave,4,20000
# Elena,5,25000

# ? Output:
# Employee(ID: 1, Name: Alice, Salary: £50000)
# Employee(ID: 2, Name: Bob, Salary: £62000)
# Employee(ID: 3, Name: Charlie, Salary: £58000)
# Employee(ID: 4, Name: Dave, Salary: £20000)
# Employee(ID: 5, Name: Elena, Salary: £25000)
