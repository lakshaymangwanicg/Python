for i in range(6):
    bill = int(input("Enter Your Total Electricity Units: "))
    extra_bill = bill-100
    other_bill = bill-200
    upper_bill = bill-400
    total = (100*5) + (100*7) + (200*10) + (upper_bill*15)
    if bill<=100:
        print(f"The Total Bill Amount is: {bill*5}")
    elif 100<bill<=200:
        print(f"The Total Bill Amount is: {(100*5) +(extra_bill*7)}")
    elif 200<bill<=400:
        print(f"The Total Bill Amount is: {(100*5) + (100*7) + (other_bill*10)}")
    else:
        print(f"The Total Bill Amount is: {(100*5) + (100*7) + (200*10) + (upper_bill*15)}")
    if total<=1000:
        print("Low")
    elif 1000<total<=3000:
        print("Medium")
    else:
        print("High")