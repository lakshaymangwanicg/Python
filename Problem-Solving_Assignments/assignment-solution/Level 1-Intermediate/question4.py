num1=int(input("Enter first Number: "))
num2=int(input("Enter secod Number: "))
num3=int(input("Enter third Number: "))


if num1>num2>num3:
    print(f"{num3} is smallar than {num2} and {num1}.")
elif num2>num3>num1:
    print(f"{num1} is smallar than {num3} and {num2}.")
elif num3>num2>num1:
    print(f"{num1} is smallar than {num3} and {num2}.")       