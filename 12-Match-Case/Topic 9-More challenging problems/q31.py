banking_type = int(input("Enter banking type: "))

match banking_type:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Balance Selected")
            case 2:
                print("Transfer Selected")
            case 3:
                print("Loan Selected")
            case _:
                print("Invalid Option Selected")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Balance Selected")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Banking Type Selected")