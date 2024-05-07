n = 30

primes = [x for x in range(2, n)
          if all(x % y != 0 for y in range(2, x))]

print(primes)