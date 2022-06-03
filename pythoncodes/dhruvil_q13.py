


def odd(l):
    c = 0
    for i in l:
        if l.count(i)%2 != 0:
            c =i
            break
    return c

print("test case [1,1,2,2,4,4,4,4,3,3,3,5,5,5,5,5]")
print('output ',odd([1,1,2,2,4,4,4,4,3,3,3,5,5,5,5,5]))