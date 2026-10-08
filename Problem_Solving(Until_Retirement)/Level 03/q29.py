num1 = int(input("Enter first Number: "))
num2 = int(input("Enter Second Number: "))
for i in range(num1,0,-1):
    if num1%i == 0 and num2%i == 0:
        print(i)