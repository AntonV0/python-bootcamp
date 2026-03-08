"""Exercise 2: Object Interaction"""


class Course:
    """Course class with attributes for course name and a list of enrolled students."""

    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []  # List to hold enrolled students

    def add_student(self, student_object):
        """Adds a student instance to the course's student list."""
        self.students.append(student_object)
        print(f"{student_object.name} enrolled in {self.course_name}")


class Student:
    """Student class with attributes for name, age, and student ID."""

    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id


if __name__ == "__main__":
    student1 = Student("Alice", 20, 1)  # Create a Student object
    course1 = Course("Mathematics")  # Create a Course object

    course1.add_student(student1)  # Enroll student1 in course1
    print(f"Course: {course1.course_name}")
    print("Enrolled Students:")
    for student in course1.students:
        print(f"{student.name} (ID: {student.student_id})")

# ? Output:
# Alice enrolled in Mathematics
# Course: Mathematics
# Enrolled Students:
# Alice (ID: 1)
