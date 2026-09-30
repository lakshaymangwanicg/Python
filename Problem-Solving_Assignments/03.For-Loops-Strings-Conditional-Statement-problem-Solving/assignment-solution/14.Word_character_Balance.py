sen = input("Enter any Sentence: ")
word = sen.split()
vowel = "aeiouAEIOU"
const = "bcdfghjklmnpqrstuvwxyzBCDFGHJKLMNPQRSTUVWXYZ"

for i in word:
    vowel_count = 0
    const_count = 0
    for name in i:
        if name in vowel:
            vowel_count+=1
        elif name in const:
            const_count+=1
    print(f"The word of sentence: {i} \n               --> Total Vowels in word == {vowel_count} \n               --> Total Consonants in word == {const_count}")
    if vowel_count > const_count:
        print("Vowles Win")
    elif const_count > vowel_count:
        print("Consonent Win")
    else:
        print("Draw")
