def square_number(n):
    """Returns the square of a number."""
    return n ** 2

def add_numbers(a, b):
    """Returns the sum of the square of the first number and the cube of the second number."""
    return (a ** 2) + (b ** 3)

# Example usage
num = int(input("Enter a number: "))
print(f"The square of {num} is {square_number(num)}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The sum of the square of {num1} and the cube of {num2} is {add_numbers(num1, num2)}")

