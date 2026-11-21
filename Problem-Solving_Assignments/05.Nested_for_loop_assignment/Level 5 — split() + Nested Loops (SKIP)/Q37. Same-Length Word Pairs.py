sen = input("Enter a String: ").split()
for i in range(len(sen)):
    for j in range(i + 1, len(sen)):
        if len(sen[i]) == len(sen[j]):
            print(sen[i], sen[j])


