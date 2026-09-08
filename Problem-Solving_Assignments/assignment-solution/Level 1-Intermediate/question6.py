num = int(input("Enter a number: "))

if num / 5 == int(num / 5) and num / 11 == int(num / 11):
    print("Divisible by both 5 and 11")
elif num / 5 == int(num / 5):
    print("Divisible only by 5")
elif num / 11 == int(num / 11):
    print("Divisible only by 11")
else:
    print("Divisible by neither")