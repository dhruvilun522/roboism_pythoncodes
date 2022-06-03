def calc(x,s,y):
    if s=='+':
        return x+y
    elif s=='-':
        return x-y
    elif s=='*':
        return x*y
    elif s=='/':
        return x/y
    else :
        print("wrong operator")
print('test case 2 , "*",6')
print('output ',calc(2,'*',6))