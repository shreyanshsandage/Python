string =  input("Enter a string: ")
for char in string:
    if string.count(char) == 1:
        print(f"The first non-repeating character is: {char}")
        break