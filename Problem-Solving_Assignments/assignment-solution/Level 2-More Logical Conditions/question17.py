first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "/":
    if second == 0:
        print("Cannot divide by zero")
    else:
        print(first / second)

else:
    print("Invalid operator")