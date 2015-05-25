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


listing = []
for i in xrange(1,21):
    if is_prime(i):
        listing.append(i)
product = reduce(lambda x,y: x*y,listing) 
product *= 4
product *= 3
product *= 2
for i in xrange(1,21):
    if product%i !=0:
        print i
print product

