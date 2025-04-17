a=str(input("Enter Name = "))
b=int(input("Enter Maths marks = "))
c=int(input("Enter English marks = "))
d=int(input("Enter Science marks = "))
e=int(input("Enter Social Science marks = "))
p=(b+c+d+e)/4
print("Your percentage =",p)
if p>=100:
    print(a,"Grade is A")
elif p>=89 :
    print(a,"Grade is B")
elif p>=79:
    print(a,"Grade is C")
elif p>=69:
    print(a,"Grade is D")
else:
    print(a,"Grade is F")
