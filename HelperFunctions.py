import numpy as np
import itertools
from itertools import permutations


# Prime factorization of k as a list of primes in increasing order, with duplicates included.
def prime(k): 
    result=[]
    i=2
    while i*i<=k:
        if (k%i==0):
            result.append(i)
            k=k/i
        else:
            i=i+1
    result.append(k)
    return result


#LCD of a and b, TODO update this.
def lcd(a,b):
    k=a
    while k%b!=0:
        k=k+a
    return(k)


 # is k prime?
def isprime(k):
    if k<2: 
        return False
    if len(prime(k))==1:
        return True
    else:
        return False


# lists primes up to limit
def primes_sieve(limit): 
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes


# list of factors of n
def factors(n):
    S=prime(n)
    F=[1]
    for x in S:
        F=F+map(lambda k: k*x, F)
    F=set(F)
    F=list(F)
    F.sort()
    return F



def number_of_factors(n):
    return len(factors(n))



def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10+sum_of_digits(n/10)

            
def factorial(n):
    prod=1
    for n in range(1,n+1):
        prod=prod*n
    return prod


#This should always return 1
def collatz(n):
    if n==1:
        return 1
    elif n%2==0:
        return 1+collatz(n/2)
    else:
        return 1+collatz(3*n+1)



def triangle(n):
    return (n*(n+1)/2)

#Sum k=a to n of f(k)
def sigma(f,a,n):
    x=0
    for k in range(a,n+1):
        x+=f(k)
    return x


#lists n in digits
def digitlist(n):
    num=n
    l=[]
    while num>0:
        l.append(num%10)
        num=num/10
    return l


# nth fibonacci number where F_0=0 and F_1=1
def fibonacci(k):
    a=0
    b=1
    c=0
    for n in range(k):
        c=a+b
        a=b
        b=c
    return a



def numdigits(k):
    c=0
    x=k
    while x != 0:
        c=c+1
        x=x/10
    return c


#aka sigma
def divisorsum(n):
    A=factors(n)
    b=reduce(lambda x,y: x+y,A)
    b=b-n
    return b


#the period of the decimal representation of 1/n
def period(n):
    while n%2==0:
        n=n/2
    while n%5==0:
        n=n/5
    if n==1:
        return 0
    a=1
    L=prime(n)
    for x in L:
        if x==n:
            k=1
            while ((10**k)-1)%x!=0:
                k=k+1
            return k

        b=period(x)
        c=L.count(x)-1
        a=lcd(a,b*(x**c))
    return a

# is A (a list) palindromic?
def palindrome(A):
    while len(A)>1:
        if A[0]!=A[-1]:
            return False
        else:
            A.pop(0)
            A.pop(-1)
    return True


#n as a binary integer.
def binary(n):
    A=[]
    a=n
    k=1
    while a>0:
        if a%(2**k)==0:
            A.append(0)
            
        else:
            A.append(1)
            a=a-(2**(k-1))
        k+=1
    return A


#Takes the least significant digit of n and puts it at the front.
def rotate(n):
    x=numdigits(n)
    k=n%10
    a=n/10+k*(10**(x-1))
    return a



def triangle(n):
    A=[]
    for x in range(n):
        A.append((x+1)*(x+2)/2)
    return A

def pentagon(n):
    A=[]
    for x in range(n):
        A.append((x+1)*(3*x+2)/2)
    return A

def hexagon(n):
    A=[]
    for x in range(n):
        A.append((x+1)*(2*x+1))
    return A


def removelastdigit(n):
    return n/10

def removefirstdigit(n):
    return n%(10**(numdigits(n)-1))

def leftprime(n):
    if numdigits(n)==1:
        return isprime(n)
    else:
        return (isprime(n) and leftprime(removefirstdigit(n)))

def rightprime(n):
    if numdigits(n)==1:
        return isprime(n)
    else:
        return (isprime(n) and rightprime(removelastdigit(n)))


def pascal(n):
    T=[[1]]
    for x in range(1,n+1):
        A=[]
        A.append(1)
        for y in range(2,x+1):   
            A.append(T[x-1][y-2]+T[x-1][y-1])
        A.append(1)
        T.append(A)
    return T
