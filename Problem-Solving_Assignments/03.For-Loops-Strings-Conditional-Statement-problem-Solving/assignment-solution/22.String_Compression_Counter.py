# # sen = input("Enter a string: ")
# # count = 0
# # for i in range(len(sen)):
# #     count = 0
# #     for j in range(len(sen)):
# #         if sen[i] == sen[j]:
# #             count += 1
# #     if i<len(sen)-1 and sen[i] != sen[i+1]:
# #         print(f"{sen[i]}{count}",end="")
# # else:print(f"{sen[i]}{count}",end="")


sen = input("Enter a string: ")
for i in range(1,len(sen),2):
    number = sen[i]
    for j in range(0,len(sen),2):
        char = sen[j]
    print(f"{int(number)*char}",end=" ")


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
