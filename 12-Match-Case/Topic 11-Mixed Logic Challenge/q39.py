role = int(input("Enter role: "))

match role:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Viewing Profile")
            case 2:
                leave_days = int(input("Enter number of leave days: "))
                if leave_days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")
            case 3:
                print("Viewing Salary")
            case _:
                print("Invalid Option Selected")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Viewing Team")
            case 2:
                print("Approving Leave")
            case 3:
                print("Viewing Reports")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Role Selected")