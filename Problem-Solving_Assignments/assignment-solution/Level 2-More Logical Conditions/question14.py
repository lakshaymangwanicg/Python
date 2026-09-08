cost_price=int(input("Enter Cost Price: "))
selling_price=int(input("Enter Selling Price: "))

if selling_price > cost_price:
    print(f"profit = {selling_price - cost_price}")
elif selling_price < cost_price:
    print(f"Lose = {cost_price-selling_price}")    

elif selling_price == cost_price:
    print("No profit and no Loss")