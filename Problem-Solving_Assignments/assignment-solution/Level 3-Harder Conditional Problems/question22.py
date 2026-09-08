balance = int(input(" Enter Balance Amount: "))
withdrawal = int(input(" Enter Withdrawal Amount: "))

if withdrawal > 0 and withdrawal % 100 == 0 and withdrawal <= balance and balance - withdrawal >= 500:
    print("Withdrawal successful")
    print("Remaining balance:", balance - withdrawal)
else:
    print("Withdrawal failed")



#     account_balance=int(input("Enter Account Balance: "))
# withdrawl_amount=int(input("Enter Withdrawl Ammount: "))
# remain = account_balance - withdrawl_amount

# if withdrawl_amount>0 and withdrawl_amount/100 and withdrawl_amount < account_balance and  remain>500:
#     print("Withdrawl successful and Remaining balance {remain}:")