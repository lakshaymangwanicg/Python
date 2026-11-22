for i in range(2,int(input("Enter a Number: "))+1):
    for j in range(2,i):
        if not i%j:break
    else:print(i,end=" ")