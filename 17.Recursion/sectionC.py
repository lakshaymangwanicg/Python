# 12. Reverse a number as a string
# Write reverse_text(text) that returns the characters of a string in reverse order using recursion.
# def reverse_text(text):
#     if len(text) <= 1:
#         return text
#     return reverse_text(text[1:]) + text[0]
# print(reverse_text("cat")) 
# print(reverse_text("a")) 
# print(reverse_text("")) 





# 13. Fibonacci number (5 marks)
# # Write fibonacci(n) that returns the nth Fibonacci number using these definitions:

# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(0))  
# print(fibonacci(1))  
# print(fibonacci(6))  





# 14. Find the maximum digit (5 marks)
# Write max_digit(n) that returns the largest digit in a non-negative integer.

# def max_digit(n):
#     if n < 10:
#         return n
#     last_digit = n % 10
#     rest_max = max_digit(n // 10)

#     if last_digit > rest_max:
#         return last_digit
#     return rest_max
# print(max_digit(4729))
# print(max_digit(555))   
# print(max_digit(0))     





# 15. Trace the return values

def mystery(n):
    if n <= 1:
        return n
    return mystery(n - 1) + mystery(n - 2)
print(mystery(4))