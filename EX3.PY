# Write a Python program that demonstrates the correct use of indentation, comments, and variables following PEP 8 guidelines. 

"""
This is a module-level docstring, describing the purpose of the script.

PEP 8 recommends using triple quotes for docstrings and limiting lines
to a maximum of 72 characters within them for readability.
"""

import sys  # Standard library imports go first


def calculate_sum(value_one, value_two):
    """
    Calculates the sum of two integer values.

    This function uses 4-space indentation and snake_case variable names
    as recommended by PEP 8.

    Args:
        value_one (int): The first value to add.
        value_two (int): The second value to add.

    Returns:
        int: The sum of value_one and value_two.
    """
    # Use a single space around operators
    result = value_one + value_two

    # Inline comments should be separated by two or more spaces from the statement
    return result  # Return the result of the calculation


# Two blank lines separate top-level functions and classes


class PepEightDemonstrator:
    """
    A class to demonstrate PEP 8 naming conventions for classes (CapWords/PascalCase).
    """

    def __init__(self, initial_value):
        """
        Initializes the class instance with an initial value.

        Methods within a class are separated by a single blank line.
        """
        self.initial_value = initial_value

    def display_message(self):
        """
        A method name also uses snake_case.
        """
        # Use single quotes consistently for strings
        message = 'Demonstrating PEP 8 compliance.'

        # Indentation for code blocks within methods also uses 4 spaces
        if self.initial_value > 0:
            print(f'{message} Initial value: {self.initial_value}')
        else:
            print(f'{message} Initial value is zero or negative.')


# Constants use UPPER_CASE_WITH_UNDERSCORES
DEFAULT_VALUE = 10
ANOTHER_VALUE = 5

if __name__ == '__main__':
    # PEP 8 recommends limiting lines to a maximum of 79 characters
    # Blank lines can be used inside functions to separate logical sections

    # Function call with snake_case variables
    total_sum = calculate_sum(DEFAULT_VALUE, ANOTHER_VALUE)

    # Creating an instance of the PascalCase class
    demonstrator_instance = PepEightDemonstrator(total_sum)

    # Calling a method
    demonstrator_instance.display_message()




