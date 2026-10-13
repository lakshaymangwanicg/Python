num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print("Invalid number")
    num = int(input("Enter a number between 1 and 10: "))

print("accepted number:", num)