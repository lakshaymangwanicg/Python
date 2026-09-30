number=int(input("Enter a Number: "))
for i in range(0,number):
    for k in range(0,number-i):
        print(" " , end="")
    for j in range(1,i+1):
        print("*", end="")
    for l in range(0,i+1):
            print("*" , end="")    
    print()   