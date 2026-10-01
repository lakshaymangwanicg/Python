number = int(input("Enter a number: "))
repeat = 0
while number > 0:
    digit = number % 10
    repeat = repeat * 10 + digit
    number = number // 10

print("Reverse:", repeat)