import math
def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True
def cirp(n):
    c=0
    x = str(n)
    for i in range(len(x)):
        x=x[1:]+x[0]
        t=int(x)
        if not(isprime(t)):
            c = 1
            break
    if c==1:
        return 0
    else:
        return 1
co=0
for i in range(2,1000000):
    co = co+cirp(i)
    print(i)
print(co)
