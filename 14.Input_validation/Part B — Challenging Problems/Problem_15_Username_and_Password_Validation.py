username = input("Enter username: ").strip()
password = input("Enter password: ")

while len(username) < 5 or " " in username or len(password.strip()) < 8:
    print("Invalid username or password")

    username = input("Enter username again: ").strip()
    password = input("Enter password again: ")

print("Login details accepted")