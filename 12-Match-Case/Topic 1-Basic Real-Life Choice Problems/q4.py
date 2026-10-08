choice = int(input("Enter Traffic Signal Color: "))

match choice:
    case red:
        print("red -> Stop")
    case yellow:
        print("yellow -> Wait")
    case green:
        print("green -> Go")
    case _:
        print("Invalid Choice")