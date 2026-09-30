total=0
first=0
second=0
third=0
for i in range(1,11):
    price = int(input(f"Enter Prices of {i} Products: "))
    if price>=5000:
        total+=price*0.2
        first+=1
        print(f"----------->  After Discount Price {price*0.2} Rupess.")
    if 3000<=price<5000:
        total+=price*0.15
        second+=1
        print(f"----------->  After Discount Price {price*0.15} Rupess.")
    if 1000<=price<3000:
        total+=price*0.1
        third+=1
        print(f"----------->  After Discount Price [{price*0.1}] Rupess.")
    print(f"----------->  Total Price of {i}th item is: [{price}]")
print(f"The Total Price of 10 Products is: [{total}] rupess.")
print(f"[{first}] items that's more than 5000")
print(f"[{second}] items that's between 3000-5000")
print(f"[{third}] items that's between 1000-3000")
