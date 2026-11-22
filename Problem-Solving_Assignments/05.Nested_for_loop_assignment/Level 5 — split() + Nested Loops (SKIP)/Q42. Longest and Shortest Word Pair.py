



























sen = input("Enter a String: ").split()
m=0
s=9999999999
m0=""
for i in sen:
    if len(i)>=m:
        if len(i)>m:
            m0=i+" "
            m=len(i)
        else:
            m0+=i+" "
    if len(i)<s:
        s=len(i)
        s0=i
print(f"Longest = {m0}; Shortest = {s0}")