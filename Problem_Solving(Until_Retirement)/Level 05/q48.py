word = input("Enter a String: ")
result = ""

for i in word:
    if i not in "aeiouAEIOU":
        result += i

print(result)
