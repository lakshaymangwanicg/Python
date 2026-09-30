for i in range(1,6):
    mem=input("Are You Member?? then write yes :")
    total=0
    print(f"Customer: {i}")
    for j in range(1,4):
        price=int(input(f"Enter Price of your item {j}: "))
    if total>=2000 and mem=="y":
        total+=price
        print(total*0.15)
    elif total>=2000:
        total+=price
        print(total*0.20)
    if 1000<=total<2000:
        total+=price
        print(total*0.1)
    elif 1000<=total<2000 and mem=="y":
        total+=price
        print(total*0.15)
    if total<1000:
        total+=price
        print(total)
    elif total<1000 and mem=="y":
        total+=price
        print(total*0.05)