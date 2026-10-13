numbers  = (input("Enter Numbers: ")).split()
target = int(input("Enter a number: "))
for num in numbers:
    if int(num)<0:
        continue
    if int(num) == target:
        print("Found", end=" ")
        break
else:
    print("Target Not Found")
