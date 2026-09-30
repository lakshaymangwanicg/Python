number=int(input("Enter your marks: "))
if number<0 or number>100:
    print("Invalid marks")
elif number>=40:
    print("Pass")
else:
    print("Fail")    
