for j in range(5):
    names = input("Enter Your Name: ")
    marks = int(input("Enter Your Marks: "))
    word = names.split()
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
        if marks>=90:
            print("A Grade")
        elif 70<=marks<90:
            print("B Grade")
        elif 40<=marks<70:
            print("C Grade")
        elif marks<40:
            print("Fail")
            
        print(f"The word of sentence: {i} \n---------------> Total Vowels in word == {vowel_count} \n---------------> Total Consonants in word == {const_count}")
        if vowel_count > const_count:
            print("Vowles Win")
        elif const_count > vowel_count:
            print("Consonent Win")
        else:
            print("Draw")


































#
# 
#  const = "bcdfghjklmnpqrstuvwxyzBCDFGHJKLMNPQRSTUVWXYZ"
# vowel = "aeiouAEIOU"
# for i in range(5):
#     const = "bcdfghjklmnpqrstuvwxyzBCDFGHJKLMNPQRSTUVWXYZ"
#     vowel = "aeiouAEIOU"
#     username=input("Enter Your Username: ")
#     marks=int(input("Enter Your Marks: "))
#     vowel_count=0
#     const_count=0
#     for name in i:
#         if name in vowel:
#             vowel_count+=1
#         elif name in const:
#             const_count+=1
    
# print(vowel_count,const_count)
