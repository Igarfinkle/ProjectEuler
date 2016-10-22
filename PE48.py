def prob48():
    a=range(1,1001)
    a=map(lambda x:x**x,a)
    b=reduce(lambda x,y:x+y,a)
    return b

