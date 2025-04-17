import random
fruit = "Banana"
colour = random.choice(["Green", "Yellow", "Brown"])
print(f"The {fruit} is {colour}")
if colour == "Green":
    print(f"The {fruit} is not ripe yet")
elif colour == "Yellow":
    print(f"The {fruit} is ripe")
else:
    print(f"The {fruit} is overripe")