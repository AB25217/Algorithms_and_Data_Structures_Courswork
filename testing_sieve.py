"""
Author: Aleksandar Bozov
File that will complete temporary testing
"""
import time
def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    for i in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

def segmented_sieve(m, n):
    limit = int(n**0.5)
    prime_numbers = sieve_of_eratosthenes(limit)
    numbers = [True] * (n - m + 1)

    for prime in prime_numbers:
        start = max(prime * prime, (m + prime - 1) // prime * prime)
        for i in range(start, n + 1, prime):
            numbers[i - m] = False

    all_prime_numbers = [i for i in range(m, n + 1) if numbers[i - m]]

    return all_prime_numbers


start_time = time.time()
#print(sieve_of_eratosthenes(10000))
print(segmented_sieve(15_000_000_000,100_000_000_000))
print(time.time() - start_time)