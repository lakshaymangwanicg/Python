num = int(input("Enter a number between 1 and 100: "))

while num < 1 or num > 100:
    print("Invalid numbe")
    num = int(input("Enter a number between 1 and 100: "))

print("Accepted number:", num)