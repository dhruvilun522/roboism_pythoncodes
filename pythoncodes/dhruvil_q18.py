l=['north','south','south','east','west','north','west']
print('test case',l)
x = min(l.count("north"),l.count("south"))
y = min(l.count("east"),l.count("west"))
for i in range(x):
    l.remove("north")
    l.remove("south")
for i in range(y):
    l.remove("east")
    l.remove("west")
print('output',l)