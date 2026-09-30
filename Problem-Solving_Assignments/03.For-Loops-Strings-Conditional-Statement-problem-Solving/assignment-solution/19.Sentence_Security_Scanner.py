sentence= input("Enter Your Sentence Here: ")
digit = speical_chr = url = 0
for i in password:
    if i =='.':
        url+=1
    elif i>='a' and i<='z':
        lower+=1
    if i>='0' and i<='9':
        digit+=1
    else:
        speical_chr+=1
