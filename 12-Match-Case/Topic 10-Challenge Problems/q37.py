category = int(input("Enter category: "))

match category:
    case 1:
        course = int(input("Enter course: "))
        match course:
            case 1:
                print("Python Selected")
            case 2:
                print("Java Selected")
            case 3:
                print("C++ Selected")
            case _:
                print("Invalid Course Selected")
    case 2:
        course = int(input("Enter course: "))
        match course:
            case 1:
                print("Algebra Selected")
            case 2:
                print("Calculus Selected")
            case 3:
                print("Statistics Selected")
            case _:
                print("Invalid Course Selected")
    case 3:
        course = int(input("Enter course: "))
        match course:
            case 1:
                print("English Selected")
            case 2:
                print("Presentation Selected")
            case 3:
                print("Interview Skills Selected")
            case _:
                print("Invalid Course Selected")
    case _:
        print("Invalid Category Selected")