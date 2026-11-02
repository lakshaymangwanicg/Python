word = input("Enter a String: ")
for i in word:
    for j in word:
        if i == j:
            continue
        else:
            print(f"{i} {j}")