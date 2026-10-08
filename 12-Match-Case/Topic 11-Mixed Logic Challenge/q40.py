role = int(input("Enter role: "))

match role:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Option Selected")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Students List")
            case 2:
                print("Opening Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Option Selected")
    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Fees Management")
            case 2:
                print("Opening Admissions Portal")
            case 3:
                print("Opening Notices Board")
            case 4:
                print("Opening Departments")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Role Selected")