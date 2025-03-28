a = input("Enter Username: ")
b = int(input("Enter username age: "))
if b <= 13:
    print(f"{a} is a Child")
elif b <= 19:
    print(f"{a} is a Teenager" )
elif b <= 59:
    print(f"{a} is a Adult" )
else:
    print(f"{a} is a Senior" )