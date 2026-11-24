num = int(input("Enter a Number: "))
for i in range(num):
    for k in range(1,num-i):
        print(" " , end="")
    for j in range(1,i+1):
        print("*", end="")
    for l in range(0,i+1):
            print("*" , end="")    
    print()   


for i in range(num-1,0,-1):
    for k in range(0,num-i):
        print(" " , end="")
    for j in range(1,i+1):
        print("*", end="")
    for l in range(2,i+1):
        print("*" , end="")    
    print()   
