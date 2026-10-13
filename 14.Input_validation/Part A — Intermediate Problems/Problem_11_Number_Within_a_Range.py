num = int(input("Enter a number between 10 and 50: "))

while num < 10 or num > 50:
    print("Invalid number")
    num = int(input("Enter a number between 10 and 50: "))

if num % 2 == 0:
    print("even number")
else:
    print("odd number")