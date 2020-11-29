

primes = [2, 3, 5, 7]
for i in range(11, 1000):

    is_prime = True
    for p in primes:
        if i % p == 0:
            is_prime = False
            break

        if p >= i:
            break

    if is_prime:
        primes.append(i)

for p in primes:
    print(p)
