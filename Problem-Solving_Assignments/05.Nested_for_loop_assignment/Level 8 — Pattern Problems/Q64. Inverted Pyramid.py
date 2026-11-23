num = int(input("Enter a Number: "))
for i in range(1,num+1):
    for k in range(i):
        print(" ",end="")
    for j in range(1,2*(num-i)+2):
        print(j,end="")
    print()