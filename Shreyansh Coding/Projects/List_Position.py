a = int(input("Enter your number: "))

list_one = [5, 7, 1, 3, 8, 4, 9, 23, 86, 40]

if a in list_one:
    position = list_one.index(a)  
    print(f"The value {a} is found at index {position}.")
else:
    print(f"The value {a} is not in the list.")
