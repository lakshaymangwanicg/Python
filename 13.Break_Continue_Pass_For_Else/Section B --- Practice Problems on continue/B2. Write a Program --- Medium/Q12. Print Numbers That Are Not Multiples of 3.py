number = int(input("enter a integer: "))
for i in range(number):
    if i%3 == 0:
        continue
    print(i , end=" ")