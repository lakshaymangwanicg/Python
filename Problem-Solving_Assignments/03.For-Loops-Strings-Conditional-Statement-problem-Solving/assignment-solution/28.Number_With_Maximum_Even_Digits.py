eve="02468"
od="13579"
highvalue = -1
highword = ""
for i in range(1,11):
    even=0
    odd=0
    number = int(input(f"Enter {i} Integer: "))
    number = str(number)
    for j in number:
        if j in eve:
            even+=1
        elif j in od:
            odd+=1
    print(f"{even} Even and {odd} Odd Integer.")
    if even > highvalue:
        highvalue = even
        highword = number
        
print(f"The Highest Even Number is: {highvalue} and The Number is {highword})")