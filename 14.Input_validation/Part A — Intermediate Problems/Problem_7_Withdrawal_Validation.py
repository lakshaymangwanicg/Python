balance = 5000

amount = int(input("Enter withdrawal amount: "))

while amount <= 0 or amount > balance:
    print("Invalid withdrawal amount")
    amount = int(input("Enter withdrawal amount again: "))

balance -=amount

print("Withdrawal successful")
print("Remaining balance:", balance)