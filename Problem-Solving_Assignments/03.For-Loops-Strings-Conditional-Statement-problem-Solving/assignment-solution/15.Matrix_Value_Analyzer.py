even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0
zero_count = 0
print("Enter 9 numbers for 3 x 3 matrix:")
for i in range(3):
    for j in range(3):
        num = int(input(f"Enter number {i}{j}: "))
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
print("Even count:", even_count) 
print("Odd count:", odd_count)
print("Positive count:", positive_count)
print("Negative count:", negative_count)
print("Zero count:", zero_count)
