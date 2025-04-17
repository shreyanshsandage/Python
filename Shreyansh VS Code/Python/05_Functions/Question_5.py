name = input("Enter your name: ")

def greet_user(name="Guest"):
    return f"Hello, {name}!"

print(greet_user(name)) 
print(greet_user())     