def calcsum(s):
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
    return sum
print("test case 'h1 dhru45 2pa3'")
print('output ',calcsum("h1 dhru45 2pa3"))
