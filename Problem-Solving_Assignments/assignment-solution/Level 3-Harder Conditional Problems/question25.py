marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))


if marks1 < 0 or marks1 > 100 or marks2 < 0 or marks2 > 100 or marks3 < 0 or marks3 > 100:
    print("Invalid marks")
elif marks1 < 35 or marks2 < 35 or marks3 < 35:
    print("Fail")
    
average = (marks1 + marks2 + marks3) / 3
if average >= 75:
    print("Distinction")
elif average >= 60:
    print("first class")
elif average >= 50:
    print("second class")
else:
    print("Pass")