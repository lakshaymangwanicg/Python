word = input("Enter a Word: ")
vowel = "AEIOUaeiou"
for i in range(len(word)):
    if word[i] in vowel:
        print(f"{word[i]} = Vowel")
    else:
        print(f"{word[i]} = Consonant")