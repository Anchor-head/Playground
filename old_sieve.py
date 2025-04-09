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



def pick_prime(primes, min_size=1000):

    """returns the first prime greater than your minimum size"""

    for prime in primes:

        if prime >= min_size:

            return prime

    # if no prime large enough exists, use last one on list

    return primes[-1]



def hash(string, modulus, p=31):
# p should be greater than the number of different possible characters in strings
# default p=31 is for lowercase letter-only strings; use p=53 for mixed case strings,
# or even higher prime values of p if strings may include numbers and special characters too.

    """implements polynomial rolling hash on string"""
    
    hash_value = 0
    power=1
    
    for char in string:

        hash_value += ord(char)*power
        power *= p

    return hash_value % modulus



if __name__ == '__main__':
# example test case

    # generate primes list to use as modulus
    primes = sieve(10000) # modify limit based on your needs


    # find a fitting prime modulus for rolling hash
    modulus = pick_prime(primes, 1000) # min_size is typically much bigger than this to avoid collision


    # words to hash as a test
    test_array = ["alpha","beta","gamma","delta","epsilon"]



    for string in test_array:

        hash_value = hash(string, modulus)

        print(f"Hash of {string} is {hash_value}")
    
    print(modulus)