# 06. Predict the output:

value = 100
def test():
    value = 200
    print(value)
test()
print(value)



# 07. Fix this code so it increments the global variable:

clicks = 0
def click():
    click = clicks + 1
    print(click)
click()


# 08. Explain why this code raises an error:

name = "Asha"
def show():
    name = "Ravi"
    print(name)
show()


# 09. Write a nested function that reads a variable from its enclosing function.

def hlo():
    msg = "Hello"
    def hloo():
        print(msg)
    hloo()
hlo()