n=int(input("Enter a Number: "))
for j in range(n,0,-1):
    for k in range(j):
        print("*",end=" ")
    print()