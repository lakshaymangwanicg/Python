sen = input("Enter a String: ").split()
for i in range(len(sen)):
    for j in range(i + 1, len(sen)):
        if sen[i][0] == sen[j][0]:
            print(sen[i], sen[j])

