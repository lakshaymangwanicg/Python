# 01. Create a function with a local variable city and print it.

def show_city():
    city="Surat"
    print(city)
show_city()


# 02. Create a global variable school. Read it inside a function.

school="Engineer Points"
def show_school():
    print(school)
show_school()

# 03. Assign a variable inside an if block and print it outside the block.

flag=True
if flag:
    message="inside condition"
print(message)

# 04. Use a for loop to assign a loop variable. Print it after the loop.

for i in range(1,6):
    print(i)
print(f"after loop: {i}")

