number=int(input("Enter a number: "))
if number>0 and number%2==0:
    print("Positive Even")
elif number>0 and number%2==1:
    print("Positive Odd")
elif number<0 and number%2==0:
    print("Negative Even")
elif number<0 and number%2==1:
    print("Negative Odd")
elif number==0:
    print("Zero")            