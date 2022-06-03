def ordlist(l,s):
    if s in ('asc','desc'):
        for i in range(len(l)):
            for j in range(len(l)-i-1):
                if l[j]>l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]
        if s=="asc":
            return l
        else:
            return l[::-1]
    elif s=='none':
        return l
    else:
        print("wrong argument")
l=[1,3,4,2]
print('test case l=[1,2,3,4],desc')
print(ordlist(l,"desc"))
