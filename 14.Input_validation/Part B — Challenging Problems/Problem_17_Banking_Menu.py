balance = 10000

choice = 0

while choice != 4:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))

        while amount <= 0:
            print("amount must be greater than zero.")
            amount = int(input("Enter deposit amount again: "))

        balance = balance + amount
        print("new balance:", balance)

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))

        while amount <= 0 or amount > balance:
            print("Invalid withdrawal amount")
            amount = int(input("Enter withdrawal amount again: "))

        balance = balance - amount
        print("remaining balance:", balance)

    elif choice == 4:
        print("thank you")

    else:
        print("Invalid choice")
        choice = 0