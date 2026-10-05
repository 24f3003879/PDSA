def isprime(n):
    if n <= 1:
        return False
    else:
        prime = True
        for i in range(2, int(n**0.5) + 1):
            if n%i == 0:
                prime = False
                break
        return prime


print(isprime(9))
print(isprime(10))

