for i in range(5):
    email = input("Enter email: ").strip()
    email2=email.split("@")
    if email.count("@") == 1 and " " not in email and email2[0] != "" and email2[1] != "" and "." in email2[1]:
        print("Valid")
    else:
        print("Invalid")
