total=0
first=0
second=0
third=0
fourth=0
for i in range(1,9):
    price = int(input(f"Enter Salary of Employess Number {i} : "))
    total+=price
    if price>=100000:
        first+=1
        print("Executive")
    if 50001<=price<100000:
        second+=1
        print("Senior")
    if 25000<=price<=50000:
        third+=1
        print("Mid")
    if price<25000:
        fourth+=1
        print("Junior")

print(f"[{first}] Employee have Salary more than 100000")
print(f"[{second}] Employee have Salary between 50000 - 100000")
print(f"[{third}] Employee have Salary between 25000 - 50000")
print(f"[{fourth}] Employee have Salary less than 25000")
print(f"The Average Salary is: {(total)/8}")
