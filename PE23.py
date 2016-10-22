def prob23():
    F=[]
    for x in range(10,28123):
        if x<divisorsum(x):
            F.append(x)
    print(F)
    L=[]
    for x in F:
        for y in F:
            if x+y < 28123:
                L.append(x+y)
    L=list(set(L))
    print(L)
    a=0
    for x in range(0,28123):
        if x not in L:
            a=x+a
    print(a)
