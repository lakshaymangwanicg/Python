# 21. --->
# Define analyze_number(number) that returns three values: the absolute value, whether it is even, and the number of digits. Do not use abs(); assume the input is an integer.

# def analyze_number(number):
#     if number%2 == 0:
#         return (((number)*(-1)),len(str(number))-1)
#     return ("Enter only even Number")
# print(analyze_number(-344))







# 22. ----->
# Define calculate_stats(a, b, c) that returns the smallest, largest, and sum of three numbers.

# def calculate_stats(a, b, c):
#     if a>b>c:
#         return (f"smallest number is {c} and the largest number is {a} ")
#     elif a>c>b:
#         return (f"smallest number is {b} and the largest number is {a} ")
#     elif b>c>a:
#         return (f"smallest number is {a} and the largest number is {b} ")
#     elif b>a>c:
#         return (f"smallest number is {c} and the largest number is {b} ")
#     elif c>a>b:
#         return (f"smallest number is {b} and the largest number is {c} ")
#     else:
#         return (f"smallest number is {a} and the largest number is {c} ")
# print(calculate_stats(11,45,33))







# 23. ------>
# Define make_sentence(subject, verb, object) that returns a sentence. Call it with keyword arguments in a different order.

# def make_sentence(subject, verb, objects):
#     return subject + " " + verb + " " + objects
# print(make_sentence(verb="is", subject="He", objects="boy."))





# 24. ----->
# Define apply_discount(price, discount=0) that returns the final price after subtracting the discount percentage. Assume discount is between 0 and 100.

# def apply_discount(price, discount=0):
#     return price - (price*discount)/100
# print(apply_discount(price = 20000, discount=13.43))





# 25. ------>
# Define calculate_pay(hours, rate=200, bonus=0) that returns hours * rate + bonus. Try different combinations of positional and keyword arguments.

# def calculate_pay(hours, rate=200,bonus = 2):
#     return hours * rate + bonus
# print(calculate_pay(21))