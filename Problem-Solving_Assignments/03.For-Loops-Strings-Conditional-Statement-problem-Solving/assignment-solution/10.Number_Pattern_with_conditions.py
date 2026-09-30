n = int(input("Enter Row Number: "))
for i in range(n):
    for j in range(1,2*i+2):
        if j%3==0 and j%5==0:
            print("Z",end=" ")
        elif j%3==0:
            print("X",end=" ")
        elif j%5==0:
            print("Y",end=" ")
        else:
            print(j,end=" ")    
    
        

        




        # if j%2==0:
        #     print("2", end=" ")
        # elif j%3==0:
        #     print("X", end=" ")
        # elif j%4==0:
        #     print("4", end=" ")
        # elif j%5==0:
        #     print("Y", end=" ")
        # if j%3==0 and j%5==0:
        #     print("Z", end=" ")    

    print()

