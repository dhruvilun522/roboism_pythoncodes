def crednum(s):
    a = ""
    for i in range(len(s)):
        if i<(len(s)-4):
            a = a+'*'
        else:
            a = a + s[i]
    return a
print('test case 1234567890')
print('output ',crednum("1234567890"))