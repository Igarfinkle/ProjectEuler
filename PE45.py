
def prob45(n):
    T=set(triangle(n))
    P=set(pentagon(n))
    H=set(hexagon(n))
    for x in H:
        if x in T and x in P:
            print x