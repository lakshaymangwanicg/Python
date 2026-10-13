numbers  = (input("Enter Numbers: ")).split()
for num in numbers:
    if int(num) == 0:
        continue
    if int(num) == -1:
        break
else:
    print("All values processed")
