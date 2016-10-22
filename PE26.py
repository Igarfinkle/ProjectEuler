def prob26():
    a=1
    for x in range(2,1000):
        k=period(x)
        if k>a:
            a=x 
    return a