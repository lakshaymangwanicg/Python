sen = input("Enter a String: ").split()
for i in range(len(sen)):
    for j in range(i + 1, len(sen)):
        if sen[i][-1] == sen[j][-1]:
            print(sen[i], sen[j]) z