def greet(name):
    print("Hello", name)

greet("Asha")
greet("Rahul")




def subtract(a, b):
    return a - b

print(subtract(8, 3))
print(subtract(3, 8))




def calculate(number):
    return number * 2

result = calculate(5)
print(result + 3)





def greet(name="Guest"):
    return "Hello " + name

print(greet())
print(greet("Asha"))





def values():
    return 10, 20

a, b = values()
print(a + b)





def show(a, b=5):
    print(a, b)

show(10)
show(10, 20)
show(a=7, b=3)






def demo():
    print("A")
    return 5
    print("B")

print(demo())





def total(a, b, c=10):
    return a + b + c

print(total(1, c=3, b=2))

