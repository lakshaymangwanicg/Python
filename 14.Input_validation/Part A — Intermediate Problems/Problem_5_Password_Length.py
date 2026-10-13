password = input("Enter your password: ")

while len(password.strip()) < 8:
    print("Password must have at least 8 characters.")
    password = input("Enter your password again: ")

print("Password accepted")