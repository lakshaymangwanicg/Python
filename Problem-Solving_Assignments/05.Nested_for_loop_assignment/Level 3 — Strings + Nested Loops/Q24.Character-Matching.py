str1 = input("Enter a String: ")
str2 = input("Enter a String: ")
for i in str1:
    for j in str2:
        if i == j:
            print(f"{i} {j}")
