passed = 0
good = 0
excellent = 0
fail = 0
invalid = 0
for number in range(1,11):
    number=int(input("Every Student Enter Marks Here: "))
    if 35<=number<=49:
        print("pass")
        passed+=1
    elif 50<=number<=74:
        print("Good")
        good+=1
    elif 75<=number<=100:
        print("Excellent")
        excellent+=1
    elif 0<=number<=35:
        print("Fail")
        fail+=1
    else:
        print("Invalid Numbers")
        invalid+=1
print(f"The Number of Passed Students is: {passed}")    
print(f"The Number of Good Studentsis: {good}")    
print(f"The Number of Excellent Students is: {excellent}")    
print(f"The Number of Fail Students is: {fail}")    
print(f"The Number of Students Who Enter Invalid Numbers is: {invalid}")    

