# 11. Use nonlocal to create a counter that returns 1, 2, 3 across three calls.

def make_counter():
    count=0
    def inc():
        nonlocal count
        count+=1
        return count
    return inc
counter=make_counter()
print(counter())
print(counter())
print(counter())



# 12. Predict the output: python     x = 1     def outer():         x = 2         def inner():             x = 3             print(x)         inner()         print(x)     outer()     print(x)


x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print(x)
    inner()
    print(x)
outer()
print(x)


# 13. Explain why the loop variable in a normal for loop can remain available after the loop, but a list-comprehension variable in Python 3 does not overwrite an outer variable.


a=100
sq=[a*a for a in range(1,4)]
print(a)

for a in range(1,4):
    pass
print(a)


# 14. Create a function that returns another function. Explain which variable remains available and why.

def into(a):
    def multiply(n):
        return n*a
    return multiply
x2=into(2)
x3=into(3)
print(x2(5))
print(x3(5))