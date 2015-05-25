fibs = [1,1]
i = 2
while fibs[i-1] < 4000000:
    fibs.append(fibs[i-1]+fibs[i-2])
    i += 1

fibs = fibs[:-1]

summa = 0
for fib in fibs:
    if fib%2==0:
        summa += fib
print summa
    
