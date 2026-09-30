amount = int(input("Enter Your Ammount: "))
for i in range(7):
    trans = input(f"If You want to Deposit Then write:----> deposite \nIf You want to Withdrawal Your Amount Then write:---->withdrawal\n-->")
    if trans == "deposite":
        deposite = int(input("Enter Deposite Amount: "))
        amount = deposite + amount
    elif trans =="withdrawal":
        withdrawal = int(input("Enter Withdrawal Amount: "))
        amount = amount - withdrawal
    elif amount<0:
        amount = 0
    if amount<1000:
        print("Low Balance")
print(f"The Total Amount After 7 Day Transactions is: {amount}")
