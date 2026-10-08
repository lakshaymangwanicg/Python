choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Wi-Fi")
    case 2:
        print("bluetooth")
    case 3:
        print("Mobile Data")
    case 4:
        print("Airplane Mode")
    case 5:
        print("Exit")
    case _6:
        print("Invalid Setting")