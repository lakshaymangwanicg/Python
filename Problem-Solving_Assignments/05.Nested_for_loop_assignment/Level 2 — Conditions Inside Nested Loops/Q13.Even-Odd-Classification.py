for i in range(4):
    for j in range(4):
        if (i+j)%2 == 0:
            print("E",end=" ")
        else:
            print("O", end=" ")
    print()