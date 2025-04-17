def square_number(n):

    return n ** 2

def add_numbers(a, b):
    return (a ** 2) + (b ** 3)


num = int(input("Enter a number: "))
print(f"The square of {num} is {square_number(num)}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The sum of the square of {num1} and the cube of {num2} is {add_numbers(num1, num2)}")

