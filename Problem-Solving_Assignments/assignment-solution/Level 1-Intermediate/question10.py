age=int(input("Enter your age: "))
if age<0:
    print("Invalid Age")
elif age<18:
    print("Cannot Vote")
elif 12<age<120:
    print("Can Vote")
if age>120:
    print("Reject")           