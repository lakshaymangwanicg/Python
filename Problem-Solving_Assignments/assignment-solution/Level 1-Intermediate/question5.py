num1=int(input("Enter first Number: "))
num2=int(input("Enter secod Number: "))
num3=int(input("Enter third Number: "))


if num1>num2>num3:
    print(f"{num1} is larger than {num2} and {num3}.")
elif num2>num3>num1:
    print(f"{num2} is larger than {num3} and {num1}.")
elif num3>num2>num1:
    print(f"{num3} is larger than {num2} and {num1}.")  