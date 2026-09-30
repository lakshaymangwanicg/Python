a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    if a==b==c:
        print("Valid triangle and Equilateral")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("Valid triangle and Isosceles")
    else:
        print("Valid triangle and Scalene")
else:
    print("Invalid triangle")                   