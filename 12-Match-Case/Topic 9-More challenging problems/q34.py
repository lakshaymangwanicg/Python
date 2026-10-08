choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Start Game Selected")
    case 2:
        print("Load Game Selected")
    case 3:
        setting_choice = int(input("Enter settings option: "))
        match setting_choice:
            case 1:
                print("Sound Settings Selected")
            case 2:
                print("Graphics Settings Selected")
            case 3:
                print("Controls Settings Selected")
            case _:
                print("Invalid Settings Choice")
    case 4:
        print("Exiting Game...")
    case _:
        print("Invalid Choice")