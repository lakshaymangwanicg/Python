numbers  = (input("Enter Numbers: ")).split("-")

for num in numbers:
    if int(num) < 40:
        continue
    print(num, end=" ")
