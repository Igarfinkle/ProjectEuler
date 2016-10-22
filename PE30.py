def prob30():
    l1=[]
    for n in range(2,1000000):
        if sum(map(lambda x: x**5,digitlist(n)))==n:
            l1.append(n)
    return l1