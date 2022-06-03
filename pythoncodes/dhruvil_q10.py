def swap(a,b):
    a,b= (a^b)^a,(a^b)^b
    return a,b
print("test case (10 , 200)")
print('output ',swap(10,200))

