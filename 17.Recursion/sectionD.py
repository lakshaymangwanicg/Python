# 16. Fix the factorial

# def factorial(n):
#     if n == 0:
#         return 1

#     return n * factorial(n - 1)
# print(factorial(0))

# 17. Make progress 
# count = 0
# def stop_at_zero(n):
#     if n == 0:
#         global count
#         count +=1
#         return count
#     return stop_at_zero(n-1)
# print(stop_at_zero(5))
def stop_at_zero(n):
    if n == 0:
        return
    print(n)
    stop_at_zero(n - 1)
stop_at_zero(5)



def stop_at_zero(n):
    if n == 0:
        return
    stop_at_zero(n - 1)
    print(n)
stop_at_zero(5)