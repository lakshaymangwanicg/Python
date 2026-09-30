sen = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
highvalue = -1
lowvalue = 110000000
highword = ""
lowword = ""
words = sen.split()
for word in words:
    current_score = 0
    vowel_start = 0
    vowel_end = 0
    digit = 0
    for char in word:
        if char in words:
            current_score += 1
        elif char.isalpha():
            current_score += 1
        elif char.isdigit():
            digit+=1
        else:
            print("Invaid")
        if word[0] in vowels:
            vowel_start+=1
        if word[-1] in vowels:
            vowel_end+=1


        
    
    print(f"Word: '{word}' -> Score: {current_score}")

    if current_score > highvalue:
        highvalue = current_score
        highword = word
    if lowvalue > current_score:
        lowvalue = current_score
        lowword = word
print(f"Word with loweset score: '{lowword}' (Score: {lowvalue})")
print(f"Word with highest score: '{highword}' (Score: {highvalue})")
print(f"The total number of word in sentence is: [{len(words)}]")
print(f"Total Numbers of words beginning with a vowel is: [{vowel_start}]")
print(f"Total Numbers of words ending with a vowel is: [{vowel_end}]")
print(f"Number of words containing digits is: [{digit}]")

