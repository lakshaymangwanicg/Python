def reverse(n):
    if n < 10:
        print(n, end="")
        return
    m = n % 10
    print(m, end="")
    reverse(n // 10)
reverse(4827)