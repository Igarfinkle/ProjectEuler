def prob39():
    A=[]
    for m in range(1,50):
        for n in range(1,m):
            if (m%2==0) ^ (n%2==0):
                print [m,n]
                A.append(m*m-(n*n)+(2*m*n)+(m*m)+(n*n))
    for x in range(1001):
        a=0
        for y in A:
            if x%y==0:
                a+=1
        if a>5:
            print [x,a]