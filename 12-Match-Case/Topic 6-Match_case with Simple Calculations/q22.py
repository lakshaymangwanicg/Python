choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

match choice:
    case 1:
        print(f"{value * 1000} meters")
    case 2:
        print(f"{value / 1000} kilometers")
    case 3:
        print(f"{value * 1000} grams")
    case 4:
        print(f"{value / 1000} kilograms")
    case _:
        print("Invalid Choice")