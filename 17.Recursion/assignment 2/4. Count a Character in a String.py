def cnt(n, l):
    if n == "":
        return 0
    if n[0] == l:
        return 1 + cnt(n[1:], l)
    else:
        return cnt(n[1:], l)
print(cnt("programming", "a"))