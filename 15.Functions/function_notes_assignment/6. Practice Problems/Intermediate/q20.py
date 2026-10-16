def bill(item, quantity=1, price=100):
    return (f"{item} has price {quantity*price} rupess.")
print(bill("banana",quantity=2,price=300))