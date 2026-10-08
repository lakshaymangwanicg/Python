choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("You Selected Pizza")
    case 2:
        print("You Selected Burger")
    case 3:
        print("You Selected Pasta")
    case _:
        print("You Selected Sandwich")