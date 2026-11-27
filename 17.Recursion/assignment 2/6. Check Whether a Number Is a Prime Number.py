def prime(n,p=2):
    if n==p:
        return True
    if n<2:
        return False
    if n%p == 0:
        return False
    return prime(n,p+1)
print(prime(2))
    

# for i in range(2,n):
#     if n%i == 0:
#         print("true")