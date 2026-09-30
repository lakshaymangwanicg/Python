ch = input("Enter a character: ")

if ch.isalpha() and len(ch) == 1:
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")