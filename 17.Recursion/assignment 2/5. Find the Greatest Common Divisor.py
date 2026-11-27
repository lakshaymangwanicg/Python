def great(m,n,p=1,k=1):
    if m%p == 0 and n%p == 0:
        k = p
    if p==n or p==m:
        return k
    return great(m,n,p+1,k)
print(great(12,36))

# a=48
# b=18
# digit = 1 
# for i in range(1,min(a,b)+1):
#     if a%i == 0 and b%i == 0:
#         digit=i
# print(digit)
