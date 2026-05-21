def calculate_sum(numbers):
    """Calculate the sum of a list of numbers"""
    total = 0
    for num in numbers:
        total += num
    return total

# Test the function
numbers = [1, 2, 3, 4, 5]
result = calculate_sum(numbers)
print(f"Sum of {numbers} is {result}")
