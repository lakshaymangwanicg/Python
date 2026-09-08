purchase = float(input("Enter purchase amount: "))
if purchase < 500:
    discount_percent = 0
    discount_amount = (purchase * discount_percent) / 100
    print(f"original Amount: {purchase}")
    print("0%")
    print(f"{(purchase * discount_percent) / 100}")
    print(purchase - discount_amount)
elif purchase < 1000:
    discount_percent = 5
    discount_amount = (purchase * discount_percent) / 100
    print(f"original Amount: {purchase}")
    print("Discounnt Percentage: 5%")
    print(f"Discount Amount: {(purchase * discount_percent) / 100}")
    print(f"Final Amount: {purchase - discount_amount}")
elif purchase < 2000:
    discount_percent = 10
    discount_amount = (purchase * discount_percent) / 100
    print(f"original Amount: {purchase}")
    print("Discounnt Percentage: 10%")
    print(f"Discount Amount: {(purchase * discount_percent) / 100}")
    print(f"Final Amount: {purchase - discount_amount}")
elif purchase < 5000:
    discount_percent = 15
    discount_amount = (purchase * discount_percent) / 100
    print(f"original Amount: {purchase}")
    print("Discounnt Percentage: 15%")
    print(f"Discount Amount: {(purchase * discount_percent) / 100}")
    print(f"Final Amount: {purchase - discount_amount}")
else:
    discount_percent = 20
    discount_amount = (purchase * discount_percent) / 100
    print(f"original Amount: {purchase}")
    print("Discounnt Percentage: 20%")
    print(f"Discount Amount: {(purchase * discount_percent) / 100}")
    print(f"Final Amount: {purchase - discount_amount}")


