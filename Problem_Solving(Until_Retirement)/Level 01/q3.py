num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))
if num1>num2>num3 or num1>num3>num2:
    print(num1)
elif num2>num3>num1 or num2>num1>num3:
    print(num2)
else:
    print(num3)