def is_palindrome(n):
    tmp = str(n)
    if tmp == tmp[::-1]:
        return True
    else:
        return False
listing = []
for i in xrange(700,1000):
    for j in xrange(700,1000):
        product = i*j
        if is_palindrome(product):
            listing.append(product)
print max(listing)
        
    
