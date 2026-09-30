n = int(input("Enter Row Number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j*i%5==0:
            print("F",end="  ")
        elif j*i%2==1:
            print("O",end="  ")
        elif j*i%2==0:
            print("E",end="  ")
    print()