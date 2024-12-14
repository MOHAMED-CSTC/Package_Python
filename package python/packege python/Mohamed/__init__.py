# __init__.py

from .module1 import filter_even_numbers, find_max_number, categorize_numbers
from .module2 import number_generator, log_decorator, calculate_square, multiply
from .module3 import Calculator

__all__ = [
    "filter_even_numbers",
    "find_max_number",
    "categorize_numbers",
    "number_generator",
    "log_decorator",
    "calculate_square",
    "multiply",
    "Calculator",
]
