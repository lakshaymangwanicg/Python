marks = int(input("Enter your marks: "))

while marks < 0 or marks > 100:
    print("Invalid marks!")
    marks = int(input("Enter your marks again: "))

print("Your marks are:", marks)