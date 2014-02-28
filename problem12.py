from itertools import count, combinations
from collections import defaultdict

from problem11 import multiply

g_divisors = defaultdict(list)


def get_prime_divisors(number):
    prime_divisors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            prime_divisors.append(divisor)
            number //= divisor
            divisor = 2
        else:
            divisor += 1
    return prime_divisors


def get_divisors(number):
    divs = get_prime_divisors(number)
    divisors = {1}
    for l in range(1, len(divs) + 1):
        for combination in combinations(divs, l):
            divisors.add(multiply(combination))

    return divisors


def get_divisors_naive(number):
    return (x for x in xrange(1, number + 1) if number % x == 0)


def length(iterable):
    return sum(1 for x in iterable)


def iter_triangle_numbers():
    current_number = 1
    for x in count(2):
        yield current_number
        current_number += x


def main():
    # print get_divisors(28)
    # print zip(iter_triangle_numbers(), range(7))[-1]
    first = (x for x in iter_triangle_numbers() if length(get_divisors4(x)) > 500).next()
    print get_divisors4(first)
    print first
    # print zip(range(500), iter_triangle_numbers())[-1]
    # print get_divisors4(28)


if __name__ == "__main__":
    main()