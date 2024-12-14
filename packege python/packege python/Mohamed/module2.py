# module2.py

def number_generator(n):
    """Generates numbers from 0 to n-1."""
    for i in range(n):
        yield i

def log_decorator(func):
    """A simple decorator to log function calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

# Example of lambda function
calculate_square = lambda x: x ** 2

@log_decorator
def multiply(a, b):
    """Multiplies two numbers."""
    return a * b
