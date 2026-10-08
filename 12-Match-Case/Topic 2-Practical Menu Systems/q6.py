choice = int(input("Enter category: "))

match choice:
    case 1:
        print("Electronics")
    case 2:
        print("Clothing")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")