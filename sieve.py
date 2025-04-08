import math
def sieve(limit):

    primes=[2,3,5]
    #res=[i in primes for i in range(1, limit+1)]
    res=[i in primes for i in range(1,6)]

    

    for i in range(6, limit+1):
        isprime=False
        remainder = i%60
        if remainder in [1,13,17,29,37,41,49,53]:
            for x in range(1,int(math.sqrt((i-1)/4))):
                if math.sqrt(i-4*x**2) == int(math.sqrt(i-4*x**2)):
                    isprime ^= True

        elif remainder in [7,19,31,43]:
            for x in range(1,int(math.sqrt((i-1)/3))):
                if math.sqrt(i-3*x**2) == int(math.sqrt(i-3*x**2)):
                    isprime ^= True

        elif remainder in [11,23,47,59]:
            x=2
            while True:
                if math.sqrt(3*x**2-i) == int(math.sqrt(4*x**2-i)) < x:
                    isprime ^= True
                elif math.sqrt(3*x**2-i)>=x:
                    break
                x+=1
            
        res.append(isprime)

    r = 7
    while r * r <= limit:
        if res[r]:
            for i in range(r * r, limit + 1, r * r):
                res[i] = False
        r+=2