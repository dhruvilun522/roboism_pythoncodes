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
def primes(n):
    for i in range(1,n):
        if isprime(i):
            print(i)

print('test case 50\n\n','primes below 50 are')
primes(50)