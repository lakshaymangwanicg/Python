balance = 2000

amount = int(input("Enter deposit amount: "))

while amount <= 0:
    print("Deposit must be greater than zero.")
    amount = int(input("Enter deposit amount again: "))

balance = balance + amount

print("deposit successful")
print("new balance:", balance)