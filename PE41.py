
def prob41():
    B=set(primes_sieve(10000000))
    A=permutations(range(1,8))
    for x in A:
        if x[6]+10*x[5]+100*x[4]+1000*x[3]+10000*x[2]+100000*x[1]+1000000*x[0] in B:
            print x[6]+10*x[5]+100*x[4]+1000*x[3]+10000*x[2]+100000*x[1]+1000000*x[0]