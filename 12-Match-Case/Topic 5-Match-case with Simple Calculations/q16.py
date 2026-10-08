user_type = int(input("Enter user type: "))

match user_type:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Courses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case _:
                print("Invalid Option Selected")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening View Students")
            case 2:
                print("Opening Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid User Type Selected")