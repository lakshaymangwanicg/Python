word = input("Enter a word: ")
count = 0
vowel = "aeiouAEIOU"
for i in word:
    if i in vowel:
        count+=1
print(count)