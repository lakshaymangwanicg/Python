word = input("Enter a String: ")
char = input("enter a character: ")
for i in word:
    if i == char:
        continue
    print(i , end=" ")