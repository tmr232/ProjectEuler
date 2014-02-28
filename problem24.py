from itertools import permutations, islice, takewhile, count
from math import factorial


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


PERMS = 1000000 - 1

def main():
    # print "".join(str(c) for c in nth(permutations([0,1,2,3,4,5,6,7,8,9]), PERMS))
    n_perms = list(takewhile(lambda x: x <= PERMS, (factorial(n) for n in count())))
    perms = PERMS
    digits = range(10)
    number = 0
    i = len(n_perms) - 1
    while perms > 0:
        number *= 10
        number += digits.pop(perms // n_perms[i])
        perms %= n_perms[i]
        i -= 1

    number *= 10
    number += digits.pop(0)
    print number


if __name__ == "__main__":
    main()