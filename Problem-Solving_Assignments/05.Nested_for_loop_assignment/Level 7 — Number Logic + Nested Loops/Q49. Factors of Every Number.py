num = int(input("Enter a Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        if i%j == 0:
            print(f"{i} -> {j}")
        