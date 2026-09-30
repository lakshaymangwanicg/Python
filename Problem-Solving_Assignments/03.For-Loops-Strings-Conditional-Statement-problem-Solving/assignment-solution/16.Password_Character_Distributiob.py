password = input("Enter Your Password Here: ")
upper = lower = digit = speical_chr = 0
for i in password:
    if i>='A' and i<='Z':
        upper+=1
    elif i>='a' and i<='z':
        lower+=1
    elif i>='0' and i<='9':
        digit+=1
    else:
        speical_chr+=1
print(f"Total UpperCase in Password: {upper}")
print(f"Total LowerCase in Password: {lower}")
print(f"Total Digits in Password: {digit}")
print(f"Total Speical Character in Password: {speical_chr}")