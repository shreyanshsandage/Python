import random
name = input("Enter your name : ")
age = int(input("Enter your age : "))
day = random.choice(["Wednesday", "Thursday",])
if age <= 17:
    price = 8
else:
     price = 16
if age <=17:
    print(f"{name} is a Child hence he/she will pay {price}")
else:
    print(f"{name} is a Adult hence he/she will pay {price}")
if day == "Wednesday":
    discounted_price = price - 2
    print(f"Today is {day}. So the ticket price is $2 off. Hence your price will be {discounted_price}" )