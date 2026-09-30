password = input("Enter Your Password Here: ")
digit = speical_chr = invalid_chr = 0
for i in password:
    if i>='0' and i<='9':
        digit+=1
    elif i=='_':
        speical_chr+=1
    else:
        invalid_chr+=1
print(f"Length of Password is: {len(password)}")
print(f"First Character of password is: {password[0]}")
print(f"Total Digits in Password: {digit}")
print(f"Total Underscores Character in Password: {speical_chr}")
print(f"Total Invalid Character in Password: {invalid_chr}")



# for i in range(5):
#     name=input("Enter Your Username Here: ")
#     print(len(name))
#     print(name[0])
#     if i>='0' and i<='9':
#     # for number in i:
#     #     # if number.isdigit():
#     #     #     print()
