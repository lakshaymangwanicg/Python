choice = int(input("Enter choice: "))
temp = float(input("Enter temperature: "))

match choice:
    case 1:
        fahrenheit = (temp * 9/5) + 32
        print(f"Temperature = {fahrenheit:.1f} F")
    case 2:
        celsius = (temp - 32) * 5/9
        print(f"Temperature = {celsius:.1f} C")
    case _:
        print("Invalid Choice")