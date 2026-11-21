# sen = input("Enter a string: ")
# count = 0
# for i in range(len(sen)):
#     count = 0
#     for j in range(len(sen)):
#         if sen[i] == sen[j]:
#             count += 1
#     if i<len(sen)-1 and sen[i] != sen[i+1]:
#         print(f"{sen[i]}{count}",end="")
# else:print(f"{sen[i]}{count}",end="")


sen = input("Enter a string: ")+" "
num = ""
word= ""
for i in range(len(sen)-1):
    if sen[i].isdigit():
        num+=sen[i]
    else:
        word = sen[i]
        num = ""
    if num and not(sen[i+1].isdigit()):
        print(word*int(num),end="")
        num = ""
    elif word and not(sen[i+1].isdigit()):
        print(word,end="")
        num = ""


# sen = input("Enter a string: ")
# ch=""
# count=0
# for i in range(0,len(sen)):
#     if i%2 == 0:
#         ch=sen[i]
#     elif i%2 != 0:
#         count=sen[i]
#     if ch and count:
#         print(ch * int(count),end="")
#         ch=""
#         count=0
