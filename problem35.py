from math import sqrt, log10, ceil

def make_primes(up_to):
    primes = set()
    max_prime = 2
    for number in range(2, up_to):
        for divisor in primes:
            if number % divisor == 0:
                break
        else:
            for divisor in range(max_prime + 1, int(sqrt(number))):
                if number % divisor == 0:
                    break
            else:
                primes.add(number)
                max_prime = number
                print max_prime

    return primes

def rotate(n):
    return int((n // 10) + ((n % 10) * (10 ** (ceil(log10(n))-1))))

def rotations(n):
    return (rotate)

def main():
    print rotate(1234)
    # primes = make_primes(1000000)
    # print len(primes)

if __name__ == "__main__":
    main()