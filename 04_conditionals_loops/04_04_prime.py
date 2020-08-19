'''
Print out every prime number between 1 and 100.

'''
primes=[]

for num in range(1, 100+1):
    for i in range(2, num):
        if (num % i) == 0:
            break
        else:
            print(num)
    primes.append(primes)

