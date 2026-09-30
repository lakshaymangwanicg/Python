code = input("Enter product code: ")
if len(code) == 8 and code[:3].isupper() and code[:3].isalpha() and code[3:].isdigit():
    print("Valid Product Code")
else:
    print("Invalid Product Code")


