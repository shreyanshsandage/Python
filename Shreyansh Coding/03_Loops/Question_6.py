number =int(input("Enter your number: "))
factorial = 1
while number > 0:
    factorial =factorial * number
    number =number - 1
print(f"The factorial is: {factorial}")