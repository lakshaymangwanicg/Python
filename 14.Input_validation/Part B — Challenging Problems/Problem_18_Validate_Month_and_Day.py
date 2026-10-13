month = int(input("Enter month number: "))

while month < 1 or month > 12:
    print("Invalid month")
    month = int(input("Enter month number again: "))

day = int(input("Enter day number: "))

while day < 1 or day > 31:
    print("Invalid day")
    day = int(input("Enter day number again: "))

print("month:", month)
print("day:", day)