age = int(input("Enter your age: "))

while age < 0 or age > 120:
    print("Invalid age!")
    age = int(input("Enter your age again: "))

print("Your age is:", age)