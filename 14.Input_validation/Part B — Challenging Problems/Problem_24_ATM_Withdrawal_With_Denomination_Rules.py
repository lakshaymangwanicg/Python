balance = 10000

amount = int(input("Enter withdrawal amount: "))

while amount <= 0 or amount > balance or amount % 100 != 0:
    print("Invalid amount")
    print("Enter a positive amount within your balance.")
    print("Amount must be a multiple of 100")

    amount = int(input("Enter withdrawal amount again: "))

balance -= amount

print("withdrawn amount:", amount)
print("remaining balance:", balance)