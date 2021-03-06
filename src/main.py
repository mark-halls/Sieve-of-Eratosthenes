cache = {}
primes = []
def find_primes(maxNum, primes, cache):
    # print(f"trying: {maxNum}")
    # print(maxNum, "Beginning", cache) #interestingly viewing the values makes this a recursion error, not a stack overflow
    try: 
        if maxNum == 2:
            cache[maxNum] = 2
            primes.append(maxNum)
            return
        if maxNum == 1:
            cache[maxNum] = 1
            return
        if maxNum == 0:
            return
        if cache[maxNum]:
            find_primes(maxNum - 1, primes, cache)
            return
    except:
        pass

    isPrime = maxNum
    if isPrime % 2 is not 0:
        primes.append(isPrime)
        cache[isPrime] = isPrime
    
    while isPrime % 2 == 0:
        cache[isPrime] = isPrime
        isPrime = isPrime // 2
    find_primes(maxNum - 1, primes, cache)

    
find_primes(10000, primes, cache)
primes.sort()
print(primes)