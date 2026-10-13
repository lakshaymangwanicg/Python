score1 = int(input("Enter first score: "))

while score1 < 0 or score1 > 100:
    print("Invalid score")
    score1 = int(input("Enter first score again: "))

score2 = int(input("Enter second score: "))

while score2 < 0 or score2 > 100:
    print("Invalid score")
    score2 = int(input("Enter second score again: "))

score3 = int(input("Enter third score: "))

while score3 < 0 or score3 > 100:
    print("Invalid score")
    score3 = int(input("Enter third score again: "))

total = score1 + score2 + score3
average = total / 3

print("total:", total)
print("average:", average)