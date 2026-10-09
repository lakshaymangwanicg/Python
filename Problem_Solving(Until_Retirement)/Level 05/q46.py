word = input("Enter a String: ")
count = 0
for i in word:
    if i.isupper:
        count+=1
print(count)
