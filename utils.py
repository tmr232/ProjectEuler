from functools import reduce
from itertools import combinations, count, islice
import operator
from problem21 import gen_div_sum_table


def multiply(iterable):
    return reduce(operator.mul, iterable)


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


def iter_triangle_numbers():
    current_number = 1
    for x in count(2):
        yield current_number
        current_number += x


def length(iterable):
    return sum(1 for x in iterable)


def get_proper_divisors(number):
    divisors = get_divisors(number)
    divisors.discard(number)
    return divisors


def iter_amicable_pairs(up_to):
    table = gen_div_sum_table(up_to)
    for i, n in ((i, n) for i, n in enumerate(table) if n < up_to):
        if table[n] == i:
            yield (i, n)


def amicable_numbers(up_to):
    return (x[0] for x in iter_amicable_pairs(up_to) if x[0] != x[1])


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


def triangle_number(n):
    return (n * (n + 1)) // 2