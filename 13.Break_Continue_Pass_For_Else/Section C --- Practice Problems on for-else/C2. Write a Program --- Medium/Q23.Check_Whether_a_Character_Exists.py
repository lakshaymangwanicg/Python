numbers  = (input("Enter String: ")).split()
target = (input("Enter a target: "))
for num in numbers:
    if num == target:
        print("Character exists")
        break
else:
    print("Character missing")
