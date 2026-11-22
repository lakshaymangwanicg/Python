num = int(input("Enter a Number: "))
print("Output:",end=" ")
for i in range(2,num+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(f"{i}->1,{i}",end='; ')