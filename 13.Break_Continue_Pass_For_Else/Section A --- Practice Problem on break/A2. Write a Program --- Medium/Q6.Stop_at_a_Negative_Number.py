numbers  = (input("Enter Numbers: ")).split()

for num in numbers:
    if int(num) < 0:
        break
    print(num, end=" ")
