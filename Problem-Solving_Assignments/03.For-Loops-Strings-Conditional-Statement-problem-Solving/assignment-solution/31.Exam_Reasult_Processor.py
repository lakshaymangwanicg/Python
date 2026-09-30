highvalue = -1
for i in range(1,3):
    total=0
    stu=input(f"Number {i} Student Enter Your Name:----> ")
    for j in range(1,6):
        marks=int(input(f"Enter Marks of Subject Number {j}: "))
        if 35<=marks<=100:
            total+=marks
    if (total/5)>=90:
        print("You have to get [A] Grade")
    elif (total/5)>=60:
        print("You have to get [B] Grade")
    elif (total/5)>=35:
        print("You have to get [C] Grade")
    else:
        print("You have to get Fail")
    
    print(f"Student name is: [{stu}]")
    print(f"Total Marks in 5 Subjects is: [{total}]") 
    print(f"Percentage of marks is: [{total/5}%]")

if (total) > highvalue:
    highvalue = (total/5)
print(f"The highest marks: {highvalue}")