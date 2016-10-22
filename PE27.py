
# the smallest nonnegative n for which n^2+na+b is prime
def primequad(a,b):
    n=0
    while isprime((n*n)+(n*a)+b):
        n+=1
    return n

def prob27(): 
    a=0
    b=0
    k=0
    for x in range(-1000,1001):
        for y in range(-1000,1001):
            if primequad(x,y)>k:
                k=primequad(x,y)
                a=x
                b=y
    print k
    print a
    print b
    return (a*b)