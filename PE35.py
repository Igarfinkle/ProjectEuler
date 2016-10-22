
def prob35():
    L=primes_sieve(1000000)
    A=[]
    B=[]
    for x in L:
        print x
        a=x
        k=numdigits(x)
        for i in range(k):
            A.append(a)
            a=rotate(a)
            if a not in L:
                A=[]
                break
        B=B+A
        A=[]
    B=list(set(B))
    return len(B)