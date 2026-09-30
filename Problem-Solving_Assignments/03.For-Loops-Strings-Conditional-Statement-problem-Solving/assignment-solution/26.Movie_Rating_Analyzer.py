total=0
first=0
second=0
third=0
fourth=0
five=0
for i in range(1,11):
    price = int(input(f"Enter Ratings of Movie {i} : "))
    total+=price
    if 0<=price<=3:
        first+=1
        print("Poor")
    if 3.1<=price<=5:
        second+=1
        print("Average")
    if 5.1<=price<=7:
        third+=1
        print("Good")
    if 7.1<=price<=9:
        fourth+=1
        print("Excellent")
    if 9.1<=price<=10:
        five+=1
        print("Outstanding")

print(f"[{first}] Movie Have Poor Ratings")
print(f"[{second}] Movie Have Average  Ratings")
print(f"[{third}] Movie Have Good Ratings")
print(f"[{fourth}] Movie Have Excellent  Ratings")
print(f"[{five}] Movie Have Outstanding Ratings")

print(f"The Average Rating is: {(total)/10}")