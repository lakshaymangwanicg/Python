str1 = input("Enter a String: ")
str2 = input("Enter a String: ")
count = 0
for i in str1:
    for j in str2:
        if i == j:
            count+=1
print(count)
