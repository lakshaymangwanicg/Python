username = input("Enter username: ").strip()

while len(username) < 5 or " " in username:
    print("Invalid username")
    username = input("Enter username again: ").strip()

print("Accepted username:", username)