num = int(input("enter your number: "))
count = 0
for i in range(2,num):
    if num%i ==0:
        count += 1

if count == 0:
    print("true")
else:
    print("false")