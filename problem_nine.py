for i in xrange(1,1000):
    for j in xrange(i,1000):
        c = 1000 - i - j
        if c > 0:
            if c*c == i*i + j*j:
                print c*i*j
                break


