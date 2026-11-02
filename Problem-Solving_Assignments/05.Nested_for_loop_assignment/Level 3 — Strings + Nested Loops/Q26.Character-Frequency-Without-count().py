text = input("Enter a Text: ")
counted = ""
for i in range(len(text)):
    char = text[i]
    if char not in counted:
        frequency = 0
        for j in range(len(text)):
            if text[j] == char:
                frequency += 1    
        print(f"{char} = {frequency}")
        counted += char  