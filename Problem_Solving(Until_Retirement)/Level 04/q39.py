word = input("Enter a String: ")
count = 0
for i in word:
    if i == "a" or i == "A":
        count+=1
print(count)