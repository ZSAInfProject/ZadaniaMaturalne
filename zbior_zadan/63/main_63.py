with open("ciagi.txt") as file:
    ciagi = file.read().splitlines()

dwucykliczny = []

for ciag in ciagi:
    if len(ciag) % 2 == 0:
        half = len(ciag)//2
        length = len(ciag)
        if ciag[0:half] == ciag[half: length]:
            dwucykliczny.append(ciag)

bez_dwoch_jedynek = 0

for ciag in ciagi:
    if ciag.count('11') == 0:
        bez_dwoch_jedynek += 1

converted_ciag = []

for ciag in ciagi:
    converted_ciag.append(int(ciag,2))

biggest_ciag = 0

for ciag in converted_ciag:
    if ciag > biggest_ciag:
        biggest_ciag = ciag

primes = []

for x in range(2, biggest_ciag//2):
    isPrime = True
    for num in range(2, int(x ** 0.5) + 1):
        if x % num == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(x)

minimum = float("Inf")
maksimum = float("-Inf")

double_prime = 0

for ciag in converted_ciag:
    prime_divisors = 0
    temp = ciag
    for prime in primes:
        while temp % prime == 0:
            temp /= prime
            prime_divisors += 1
        if prime_divisors > 2:
            break
    if prime_divisors == 2:
        double_prime += 1
        if ciag > maksimum:
            maksimum = ciag
        if ciag < minimum:
            minimum = ciag

with open("ciagi_wyniki.txt", "w") as file:
    file.write("63.1\n")
    file.write("Ciagi dwucykliczne: {}\n\n".format(dwucykliczny))
    file.write("63.2\n")
    file.write("W tylu ciagach nie wystepuja 2 jedynki kolo siebie: {}\n\n".format(bez_dwoch_jedynek))
    file.write("63.3\n")
    file.write("Tyle polpierwszych: {},\nMaksimum: {},\nMinimum: {}".format(double_prime, maksimum, minimum))