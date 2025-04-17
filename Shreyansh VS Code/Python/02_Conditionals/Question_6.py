import random
distance = random.randint(1, 30)
print(f"The distance to the market is {distance} km.")
if distance < 10:
    print("I'm going to walk to the market.")
elif distance < 20:
    print("I'm going to take my bicycle to the market.")
else:
    print("I'm going to drive to the market.")