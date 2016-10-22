def prob13():
    i=1
    k=1
    while i<1000:
        k=k+1
        i=numdigits(fibonacci(k))
        print(i)
    return k
    

