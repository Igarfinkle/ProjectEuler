def prob56():
    a=0
    for x in range(1,101):
        for y in range(1,101):
            a=max(a,sumdigits(x**y))
    return a