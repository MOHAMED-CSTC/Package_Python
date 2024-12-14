# module1.py

def filter_even_numbers(numbers):
    """Filters even numbers from a list."""
    return [num for num in numbers if num % 2 == 0]

def find_max_number(numbers):
    """Finds the maximum number in a list using a loop."""
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

def categorize_numbers(numbers):
    """Categorizes numbers into 'positive', 'negative', and 'zero'."""
    categories = {"positive": [], "negative": [], "zero": []}
    for num in numbers:
        if num > 0:
            categories["positive"].append(num)
        elif num < 0:
            categories["negative"].append(num)
        else:
            categories["zero"].append(num)
    return categories
