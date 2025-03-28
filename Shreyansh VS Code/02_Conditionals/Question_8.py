password = input("Enter the password: ")
if len(password) < 6:
    print("Password is too short")
    exit()
elif len(password) > 6:
    print("Password is weak")
elif len(password) > 10:
    print("Password is Medium")
else:
    print("Password is Strong")