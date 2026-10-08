num = int(input("enter your number: "))
for j in range(1,num):
    count = 0
    for i in range(1,j):
        if j%i ==0:
            count += 1
    if count==1:
        print(j)