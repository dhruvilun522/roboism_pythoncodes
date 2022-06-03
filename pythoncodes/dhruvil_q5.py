def duplicate(l):
    n=l
    for i in range(1,100):
        n.remove(i)
    return n[0]

l = []
for i in range(1,100):
    l.append(i)
l.insert(20,45)
print("test case ",l)
print("\n duplicate character was",duplicate(l))