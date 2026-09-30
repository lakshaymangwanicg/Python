count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in range(1,9):
    price=int(input("Enter Prices of Product: "))
    if price<500:
        print("Budget")
        count1+=1
    elif price>=500 and price<=1999:
        print("Regural")
        count2+=1
    elif price>=2000 and price<=4999:
        print("Premium")
        count3+=1
    elif price>=5000:
        print("Luxury")
        count4+=1    
total=count1 + count2 + count3 + count4
print(f"The Number of Budget Catogery items is: {count1}")    
print(f"The Number of Regural Catogery items is: {count2}")    
print(f"The Number of Premium Catogery items is: {count3}")
print(f"The Number of Luxuary Catogery items is: {count4}")