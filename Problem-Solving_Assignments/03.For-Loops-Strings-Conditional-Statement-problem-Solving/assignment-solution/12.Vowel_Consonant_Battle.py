sen = input("Enter any Sentence: ")
vowel = "aeiouAEIOU"
const = "bcdfghjklmnpqrstuvwxyzBCDFGHJKLMNPQRSTUVWXYZ"
vowel_count = 0
const_count = 0
for i in sen:
    if i in vowel:
            vowel_count+=1
    elif i in const:
            const_count+=1
if vowel_count > const_count:
    print("Vowles Win")
elif const_count > vowel_count:
    print("Consonent Win")
else:
    print("Draw")