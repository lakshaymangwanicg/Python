print("1. View profile")
print("2. Edit profile")
print("3. Settings")
print("4. Exit")

choice = int(input("Enter your choice: "))

while choice < 1 or choice > 4:
    print("Invalid choice!")
    choice = int(input("Enter your choice again: "))

print("Your selected option is:", choice)