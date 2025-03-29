numbers = [1, -2, 3, -4, -5, 6, -7, 8, 9, -10]
positive_numbers = 0
for number in numbers:
    if number > 0:
        positive_numbers += 1
print("Total positive numbers are", positive_numbers)