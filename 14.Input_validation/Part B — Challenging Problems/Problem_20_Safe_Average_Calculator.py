count = int(input("How many numbers do you want to enter??:  "))

while count < 1 or count > 20:
    print("Enter a count between 1 and 20.")
    count = int(input("Enter count again: "))

total = 0
i = 1

while i <= count:
    num = int(input("Enter a number: "))
    total = total + num
    i = i + 1

average = total / count

print("average:", average)