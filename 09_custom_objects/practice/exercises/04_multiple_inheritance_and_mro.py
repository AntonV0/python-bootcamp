"""Exercise 4: Multiple Inheritance and MRO"""


class Writer:
    """Simulate writing."""

    def write(self):
        print("Writing...")


class Programmer:
    """Simulate programming"""

    def code(self):
        print("Coding...")


class TechnicalWriter(Writer, Programmer):
    """TechnicalWriter class that inherits from both Writer and Programmer."""

    def print_role(self):
        print("I am a Technical Writer.")


if __name__ == "__main__":
    tech_writer1 = TechnicalWriter()

    tech_writer1.print_role()
    tech_writer1.write()
    tech_writer1.code()

    # Method Resolution Order - order in which Python looks for a method in a hierarchy of classes.
    print("Method Resolution Order:")
    for cls in TechnicalWriter.__mro__:
        print(cls)

# ? Output:
# I am a Technical Writer.
# Writing...
# Coding...
# Method Resolution Order:
# <class '__main__.TechnicalWriter'>
# <class '__main__.Writer'>
# <class '__main__.Programmer'>
# <class 'object'>
