a=str(input("Enter Name ="))
b=int(input("Enter Maths marks ="))
c=int(input("Enter English marks ="))
d=int(input("Enter Science marks ="))
e=int(input("Enter Social Science marks ="))
p=(b+c+d+e)/4
if p >= 101:
        print ("Please enter valid marks")
        exit()
print("Your percentage =",p)
if p>=90:
    print(a,"Grade is A1")
elif p>=75:
    print(a,"Grade is A2")
elif p>=70:
    print(a,"Grade is B1")
elif p>=60:
    print(a,"Grade is B2")
elif p>=50:
    print(a,"Grade is C1")
elif p>=40:
    print(a,"Grade is C2")
elif p>=30:
    print(a,"Grade is D1")
elif p>=20:
    print(a,"Grade is D2")
else:
    print(a,"Grade is E")
