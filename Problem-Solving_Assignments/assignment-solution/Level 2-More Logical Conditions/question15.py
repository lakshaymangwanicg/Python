cost_price=int(input("Enter Cost Price: "))
selling_price=int(input("Enter Selling Price: "))


if selling_price > cost_price:
    print(f"profit = {selling_price - cost_price} and profit percentage = {((selling_price - cost_price)/(cost_price))*100}%")
elif selling_price < cost_price:
    print(f"Lose = {cost_price-selling_price}  and Loss percentage = {((cost_price - selling_price)/(cost_price))*100}%")    
else:
    print("No profit and no Loss")