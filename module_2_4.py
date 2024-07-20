numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0 and i != j and j != 1:
            count += 1
    if count == 0:
        print(not_primes)
print(primes)