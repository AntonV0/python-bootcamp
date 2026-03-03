"""Class Heirarchy for Geometric Shapes"""

import math


class Shape:
    """Base class for geometric shapes."""

    def area(self):
        """Method to calculate area, to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    """Circle subclass that inherits from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    """Rectangle subclass that inherits from Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

print(f"Area of the circle: {circle.area():.2f}")
print(f"Area of the rectangle: {rectangle.area():.2f}")

# ? Output:
# ? Area of the circle: 78.54
# ? Area of the rectangle: 24.00


def calculate_total_area(shape_list):
    """Calculate the total area of a list of shapes."""
    total = 0
    for shape in shape_list:
        total += shape.area()
    return total

# This demonstrates polymorphism, as the area method is called on different
# types of shapes without needing to know their specific types.


shapes = [Circle(radius=5), Rectangle(width=4, height=6)]
print(f"Total area of shapes: {calculate_total_area(shapes):.2f}")
# ? Output:
# ? Total area of shapes: 102.54
