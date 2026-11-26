# Section B — Basic Recursive Problems

# 5. Count down
# Write countdown(n) that prints every integer from n down to 1, then prints "Done!".

# def countdown(n):
#     if n == 0:                 
#         print("Done!")
#         return
#     print(n)
#     countdown(n - 1)         
# countdown(3)




# 6. Count up (4 marks)
# Write count_up(n) that prints numbers from 1 through n in ascending order.

# def count_up_to(n):
#     if n == 1:
#         print(1)
#         return
#     count_up_to(n - 1)
#     print(n)
# count_up_to(4)




# 7. Sum from 1 to n
# Write sum_to(n) that returns the sum of all integers from 1 through n.

# def sum(a):
#     if a == 0:
#         return 0
#     return a + sum(a - 1)
# print(sum(5))




# 8. Factorial (4 marks)
# Write factorial(n) that returns n!.

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))
# print(factorial(0))



# 9. Sum of digits (4 marks)
# Write digit_sum(n) that returns the sum of the digits of a non-negative integer.
# def digit_sum(n):
#     if n < 10:
#         return n
#     return n % 10 + digit_sum(n // 10)
# print(digit_sum(472))




# 10. Power (5 marks)
# Write power(base, exponent) that returns base raised to exponent.

# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)
# print(power(2, 5))
# print(power(9, 0))
# print(power(3, 1))




# 11. Count digits (5 marks)
# Write count_digits(n) that returns the number of digits in a non-negative integer.

