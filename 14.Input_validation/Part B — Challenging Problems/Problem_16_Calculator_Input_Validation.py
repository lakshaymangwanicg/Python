num1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")

while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Invalid operator")
    operator = input("Enter operator again: ")

num2 = int(input("Enter second number: "))

while operator == "/" and num2 == 0:
    print("cannot divide by zero")
    num2 = int(input("Enter second number again: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    result = num1 / num2

print("Result:", result)