name1 = input("Enter name 1: ")
age1 = int(input("Enter age 1: "))

name2 = input("Enter name 2: ")
age2 = int(input("Enter age 2: "))

name3 = input("Enter name 3: ")
age3 = int(input("Enter age 3: "))

if age1 < age2 and age1 < age3:
    print(f"{name1} is the youngest")

elif age2 < age1 and age2 < age3:
    print(f"{name2} is the youngest")

elif age3 < age1 and age3 < age2:
    print(f"{name3} is the youngest")

elif age1 == age2 and age1 < age3:
    print(f"{name1} and {name2} are  the youngest")

elif age1 == age3 and age1 < age2:
    print(f"{name1} and {name3} are  the youngest")

elif age2 == age3 and age2 < age1:
    print(f"{name2} and {name3} are  the youngest")

else:
    print("All three people are the same age")