age = int(input("Enter Your age: "))
if 0<=age<=12:
    print("Child")
elif 12<=age<=19:
    print("teenager")
elif age>=20:
    print("Adult")
else:
    print("Invalid Age")