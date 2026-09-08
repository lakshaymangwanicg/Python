num = int(input("Enter a number: "))

if num / 3 == int(num / 3) and num / 7 == int(num / 7):
    print("Divisible by both 3 and 7")
elif num / 3 == int(num / 3):
    print("Divisible only by 3")
elif num / 7 == int(num / 7):
    print("Divisible only by 7")
else:
    print("Divisible by neither")