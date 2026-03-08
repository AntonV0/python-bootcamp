"""Exercise 3: Inheritance and Super"""


class Animal:
    """Base class representing a generic animal."""

    def make_sound(self):
        """Prints a generic sound message."""
        print("Animal makes a sound.")


class Dog(Animal):
    """Dog class that inherits from the Animal class."""

    def make_sound(self):
        """Overrides the make_sound method."""
        print("Woof!")


class Cat(Animal):
    """Cat class that inherits from the Animal class."""

    def make_sound(self):
        """Overrides the make_sound method."""
        print("Meow!")


class SuperDog(Dog):
    """SuperDog class that inherits from the Dog class."""

    def make_sound(self):
        """Overrides the make_sound method and calls the parent method."""
        super().make_sound()  # Call the make_sound method from Dog class
        print("WOOF!!!")


if __name__ == "__main__":
    animal1 = Animal()
    dog1 = Dog()
    cat1 = Cat()
    super_dog1 = SuperDog()

    print("Animal Sound:")
    animal1.make_sound()

    print("Dog Sound:")
    dog1.make_sound()

    print("Cat Sound:")
    cat1.make_sound()

    print("SuperDog Sound:")
    super_dog1.make_sound()

# ? Output:
# Animal Sound:
# Animal makes a sound.
# Dog Sound:
# Woof!
# Cat Sound:
# Meow!
# SuperDog Sound:
# Woof!
# WOOF!!!
