order_size = input("Enter the order size (small/medium/large): ")
extra_shot = input("Do you want an extra shot? (yes/no): ")
if extra_shot == "yes":
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"
print(f"Order is {coffee}")