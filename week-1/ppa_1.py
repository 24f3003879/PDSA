n = int(input())
m = int(input())

def isprime(n):
    if n <=1:
        return False
    else:
        prime = True
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                prime = False
                break
        return prime 

def Twin_primes(n, m):
    twins = []
    for i in range(n, m+1):
        if isprime(i) and isprime(i + 2) and i + 2 <= m:
            twins.append((i, i+2))
    return twins

print(Twin_primes(n, m))

