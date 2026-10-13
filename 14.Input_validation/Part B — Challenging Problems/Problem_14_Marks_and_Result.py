marks = int(input("Enter your marks: "))

while marks < 0 or marks > 100:
    print("Invalid marks")
    marks = int(input("Enter your marks again: "))

if marks >= 75:
    print("distinction")
elif marks >= 60:
    print("first Class")
elif marks >= 35:
    print("pass")
else:
    print("fail")