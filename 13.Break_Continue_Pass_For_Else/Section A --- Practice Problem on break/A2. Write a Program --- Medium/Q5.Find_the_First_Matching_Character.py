word = input("Enter a string: ").lower()
for ch in word:
    if ch == "p":
        break
    print(ch, end=" ")