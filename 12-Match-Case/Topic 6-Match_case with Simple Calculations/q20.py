num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator: ")

match operator:
    case "+":
        print(f"Result = {num1 + num2}")
    case "-":
        print(f"Result = {num1 - num2}")
    case "*":
        print(f"Result = {num1 * num2}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"Result = {num1 / num2}")
    case _:
        print("Invalid Operator")