# n = int(input("Enter a Number: "))
def sum(n):
    if n <= 10:
        return 0
    m = (n//10)%10
    return m + (sum(n//100))
print(sum(583246))
print(sum(5832460))