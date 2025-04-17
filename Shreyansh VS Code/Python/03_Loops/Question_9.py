fruits = ["apple", "banana", "cherry", "apple", "mango"]

seen = set()
for fruit in fruits:
    if fruit in seen:
        print(f"Duplicate found: {fruit}")
        break
    seen.add(fruit)
else:
    print("All elements are unique.")