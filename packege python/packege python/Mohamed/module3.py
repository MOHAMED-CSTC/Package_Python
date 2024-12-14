# module3.py

class Calculator:
    """A simple calculator class."""

    def __init__(self, name="Basic Calculator"):
        self.name = name

    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Returns the difference of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Returns the product of two numbers."""
        return a * b

# Creating an object of the Calculator class
basic_calculator = Calculator()
