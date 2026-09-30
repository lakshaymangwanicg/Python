n = input("Enter a number: ")
sum= 1
for digit in n:
    sum *= int(digit)

print("Multiply of digits:", sum)