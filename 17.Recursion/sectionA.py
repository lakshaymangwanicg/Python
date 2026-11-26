# 1. Predict the output (2 marks)
# def show(n):
#     if n == 0:
#         print("Stop")
#         return

#     print(n)
#     show(n - 1)
#     print(n)
# show(2)



# 2. Find the base case
# def total(n):
#     if n == 0:
#         return 0

#     return n + total(n - 1)




# 3. Find the bug

# def count(n):
#     if n == 0:
#         return n

#     return count(n - 1)
# print(count(2))



# 4. Print or return?

def answer(n):
    if n == 0:
        return 0

    return n + answer(n - 1)

print(answer(3))