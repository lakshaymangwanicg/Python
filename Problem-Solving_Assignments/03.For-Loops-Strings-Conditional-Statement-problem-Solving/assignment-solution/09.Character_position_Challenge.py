sen = input("Enter a sentence: ")

vowels = "aeiouAEIOU"

hvalue = -1
hword = ""


words = sen.split()

for word in words:
    current_score = 0
    
    for char in word:
        
        if char in vowels:
            current_score +=1
            
        elif char.isalpha():
            current_score += 1
            
        elif char.isdigit():
            current_score += 1
            
        else:
            current_score += 1
        
            
    print(f"Word: {word}------score: {current_score}")
    
    
    
    if current_score > hvalue:
        hvalue = current_score
        hword = word
        

print(f"Word with highest score: {hword} (Score: {hvalue})")
if current_score%2==0:
    print("Even Position")
elif current_score%2==1:
    print("Odd Position")
else:
    print("Zero Position")
