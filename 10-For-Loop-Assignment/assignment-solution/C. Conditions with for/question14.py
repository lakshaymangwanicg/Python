number=int(input("Enter a number: "))
for i in range(1,(number+1)):
    if i%3==0 and i%2==0 and i%5==0:
        print("This number divide by 2,3,and 5 both",i)
else:
    print("This number is not dividable form 2 , 3 and 5")
