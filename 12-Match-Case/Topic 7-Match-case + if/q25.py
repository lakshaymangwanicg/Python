ticket_type = int(input("Enter ticket type: "))

match ticket_type:
    case 1 | 2 | 3:
        age = int(input("Enter age: "))
        if age < 5:
            print("Free Entry")
        else:
            match ticket_type:
                case 1:
                    print("Regular Ticket Selected")
                case 2:
                    print("Premium Ticket Selected")
                case 3:
                    print("VIP Ticket Selected")
    case _:
        print("Invalid Ticket Type")