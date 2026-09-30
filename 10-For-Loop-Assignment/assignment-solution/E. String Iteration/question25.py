text = input("Enter a string: ")

count = 0
for i in text:
    if i.isupper():
        count += 1

print("Number of times 'upper case' appears:", count)