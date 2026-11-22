num = int(input("Enter a Number: "))
for i in range(1,num+1):
    for j in range(0,num-i+1):
        print("*",end="")
    print()