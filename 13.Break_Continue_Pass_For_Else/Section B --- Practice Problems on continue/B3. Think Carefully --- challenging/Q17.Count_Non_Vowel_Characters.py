name = input("Enter a String: ").lower()
count = 0
for i in name:
    if i in "aeiou":
        count+=1
print(name,(len(name)-count))