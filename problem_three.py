import math
import random
import time
from multiprocessing import Process



def gcd(a,b):
    while b != 0:
        c = a%b
        a = b
        b = c
    return a

def g(x,n):
    return (x**2 + 1)%n

def possible_factorization(n):
    factors = []
    i = 0
    while i < n:
        a = i
        b = random.randint(0,math.ceil(math.log(n)))
        while b != a:
            a = g(a,n)
            b = g(g(b,n),n)
            p = gcd(abs(b-a),n)
            if p > 1:
                if not p in factors: 
                    factors.append(p)
        i += 1

    print factors

def brute_force(n):
    factors = []
    for i in xrange(1,n/2+1):
        if n%i==0:
            factors.append(i)
    return factors

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i = 5
    while i*i <= n:
        if n%i==0 or n%(i+2)==0:
            return False
        i = i + 6
    return True

def split_range(n):
    
if __name__ == '__main__':

    p = brute_force(600851475143)
    primes = []
    for i in p:
        if is_prime(i):
            primes.append(i)
    print max(primes)


