def gcd(a,b):
    if a ==0:
        return b
    if a==b:
        return a
    if a>b:
        a,b=b,a
    a,b = b%a,a
    return gcd(a,b)
print("test case (75,50")
print('output ',gcd(75,50))