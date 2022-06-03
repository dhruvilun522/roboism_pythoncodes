#same as question 5

def duplicate(l):
    n=l
    for i in range(1,10):
        n.remove(i)
    return n[0]
l = [1,2,3,4,5,6,7,7,8,9]
print(duplicate(l))