

def prob12():
    i=1
    k=1
    while i<501:
        k=k+1
        i=factnum(triangle(k))
        print(i)
    return k
