def countchar(s):
    a,b,c=0,0,0
    for i in s:
        if i.isdigit():
            a+=1
        elif i.isalpha():
            b+=1
        else:
            c+=1
    return a,b,c
print('test case "hi 123 ##"')
print('output(no of digit,alphabet,symbol) ',countchar("hi 123 ##"))
