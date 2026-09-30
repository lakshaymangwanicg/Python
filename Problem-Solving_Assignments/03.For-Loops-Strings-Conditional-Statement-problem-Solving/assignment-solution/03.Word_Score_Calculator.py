sen = input("Enter a sentence: ")

vowels = "aeiouAEIOU"

highvalue = -1
highword = ""


words = sen.split()

for word in words:
    current_score = 0
    
    for char in word:
        if char in vowels:
            current_score += 2
        elif char.isalpha():
            current_score += 1
        elif char.isdigit():
            current_score += 3
        else:
            current_score += 4  
            
    print(f"Word: '{word}' -> Score: {current_score}")
    
    
    if current_score > highvalue:
        highvalue = current_score
        highword = word

print(f"Word with highest score: '{highword}' (Score: {highvalue})")