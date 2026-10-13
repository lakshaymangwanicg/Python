numbers  = (input("Enter Numbers: ")).split()
target = int(input("Enter a number: "))
for num in numbers:
    if int(num) == target:
        break
    print("Found", end=" ")
else:
    print("Not Found")
