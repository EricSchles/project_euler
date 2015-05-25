def sum_squares(n):
    return sum([elem*elem for elem in xrange(n+1)])

def square_sum(n):
    return reduce(lambda x,y: x + y,xrange(n+1))**2

print square_sum(100) - sum_squares(100)
