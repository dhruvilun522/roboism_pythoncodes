def sortstr(a):
    d =""
    s = list(a)
    for i in range(len(s)):
        for j in range(len(s)-i-1):
            if s[j]>s[j+1]:
                s[j],s[j+1]=s[j+1],s[j]
    return d.join(s)
print('test case "hEllO"')
print('output ',sortstr("hEllO"))