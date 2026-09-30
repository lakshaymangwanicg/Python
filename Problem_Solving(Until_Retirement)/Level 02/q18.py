number = int(input("Enter a Number: "))
for i in range(1,number+1):
    if i%3==0:
        print(i,end=" ")
    elif i==2:
        print(0)