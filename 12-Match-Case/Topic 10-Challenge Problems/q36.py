payment_type = int(input("Enter payment type: "))

match payment_type:
    case 1:
        upi_option = int(input("Enter option: "))
        match upi_option:
            case 1:
                print("Scan QR Selected")
            case 2:
                print("Enter UPI ID Selected")
            case _:
                print("Invalid Option Selected")
    case 2:
        card_option = int(input("Enter option: "))
        match card_option:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid Option Selected")
    case 3:
        wallet_option = int(input("Enter option: "))
        match wallet_option:
            case 1:
                print("Add Money Selected")
            case 2:
                print("Pay Using Wallet Selected")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Payment Type Selected")