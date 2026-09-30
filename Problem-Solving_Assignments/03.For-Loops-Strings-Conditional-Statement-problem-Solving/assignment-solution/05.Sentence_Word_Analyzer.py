short = 0
medium = 0
long = 0


sen=input("Enter any Sentence: ").split()
for i in sen:
    if len(i)<=3:
        print("short")
        short+=1
    elif len(i)>=4 and len(i)<=6:
        print("Medium")
        medium+=1
    elif len(i)>=6:
        print("Long")
        long+=1
print(len(i))
print(f"The Number of Short word is: {short}")    
print(f"The Number of Medium word is: {medium}")    
print(f"The Number of  Long word is: {long}")    
