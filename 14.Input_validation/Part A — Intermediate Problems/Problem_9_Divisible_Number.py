num = int(input("Enter a positive number: "))

while num <= 0 or num % 3 != 0 or num % 5 != 0:
    print("Invalid number!")
    num = int(input("Enter a positive number again: "))

print("Accepted number:", num)