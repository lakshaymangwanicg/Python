sen = input("Enter a string: ")
result = ""
count = 0
for i in range(len(sen)-1):

    if sen[i] == sen[i + 1]:
        count += 1

    print(count)
