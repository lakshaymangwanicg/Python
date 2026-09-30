even = 0
odd = 0
for i in range(1,6):
    number = input("Enter Five Numbers:  ") 
    for j in number:
        num=int(j) 
        if num%2==0:
            even+=1
        elif num%2==1:
            odd+=1
even+=0
odd+=0
if even>odd:
    print(f"The Number of even digit {even} and The Number of odd digit {odd} and even type occurs more than odd.")          
elif odd>even:
    print(f"The Number of even digit {even} and The Number of odd digit {odd} and odd type occurs more than even.") 
else:
    print(f"both are same even is {even} and odd is also {odd}. ")    