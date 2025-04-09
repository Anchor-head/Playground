def sieve(limit):
    
    """returns a list of all primes less than limit"""
    
    if limit < 2:

        return []

    if limit == 2:

        return [2]
    
    if limit == 3:

        return [2,3]


    primes = [2,3]
    res = [False, True, True]
    for i in range(4, limit + 1):
        res.append(False)



    i = 1
    while ((3 * i**2) + 1 <= limit) or ((3 * i**2) - (i-1)**2 <= limit): 
    #looping through all feasible values of i
        
        j = 1
        
        while (n := (4 * i**2) + (j**2)) <= limit:
        
            if (n % 12 == 1 or n % 12 == 5):
                res[n-1] ^= True

            n = (3 * i**2) + (j**2)
            if n % 12 == 7:
                res[n-1] ^= True
            
            j+=1
            
            
        while (n := (3 * i**2) + (j**2)) <= limit:
 
            if n <= limit and n % 12 == 7:
                res[n-1] ^= True
            
            j+=1
                
                
        j = i - 1 
        while ((n := (3 * i**2) - (j**2)) <= limit) and (j>0):

            if n % 12 == 11:
                res[n-1] ^= True

            j -= 1
        
        i += 1


    # now unmarking multiples of squares of primes
    r = 5
    while r <= limit:
        
        if res[r-1]:
            primes.append(r)
            for i in range(r * r, limit + 1, r * r):
                res[i-1] = False

        r += 1

    return primes

print(sieve(75))