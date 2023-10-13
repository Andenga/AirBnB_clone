# Good example

import os
import sys

MAX_VALUE = 100

def add_numbers(x, y):
    """
    Add two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """
    result = x + y
    return result

class SampleClass:
    """
    A sample class to demonstrate PEP8 compliance.
    """

    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(f"Value: {self.value}")

if __name__ == "__main__":
    total = add_numbers(10, 20)
    print(f"Total: {total}")
