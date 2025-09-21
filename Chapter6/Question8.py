limit = 1000
primes = [True] * limit

primes[0] = primes[1] = False

for index in range(2, int(limit**0.5) + 1):  # only go up to sqrt(limit)
    if primes[index]:  # if i is still marked as prime
        # set multiples of i to False
        for count in range(index*index, limit, index):
            primes[count] = False

prime_numbers = [index for index, is_prime in enumerate(primes) if is_prime]

print("Prime numbers less than 1000:")
print(prime_numbers)
