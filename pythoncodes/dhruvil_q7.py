def maxfrequency(l):
    f = 0
    max = 0
    for i in l:
        c = l.count(i)
        if c>f:
            f=c
            max = i
    return max
print('test case [1,2,3,2,4,5,3,3,3,5,5,6,1]')
print('output ',maxfrequency([1,2,3,2,4,5,3,3,3,5,5,6,1]))