word = input("Enter a String: ").split()
for k in range(3):
    for i in word:
        for j in i:
            print(j, k)
    print()