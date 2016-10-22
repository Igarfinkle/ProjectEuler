

def prob40(n):
    A=0
    x=0
    while x<n:
        A+=1
        x+=numdigits(A)
    print x-n
    return A
