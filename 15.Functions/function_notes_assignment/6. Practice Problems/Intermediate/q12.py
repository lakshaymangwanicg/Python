def count_digits(number):
    if number == 0:
        return 1
    count = 0
    while number > 0:
        number = number // 10
        count += 1
    return count


print(count_digits(4444))