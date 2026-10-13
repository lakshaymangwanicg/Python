quantity = int(input("Enter quantity: "))

while quantity <= 0:
    print("quantity must be positive")
    quantity = int(input("Enter quantity again: "))

price = int(input("Enter unit price: "))

while price <= 0:
    print("price must be greater than zero")
    price = int(input("Enter price again: "))

total = quantity * price

print("total cost:", total)