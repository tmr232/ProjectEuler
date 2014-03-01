from collections import defaultdict
from utils import iter_triangle_numbers, length, get_divisors

g_divisors = defaultdict(list)


def get_divisors_naive(number):
    return (x for x in xrange(1, number + 1) if number % x == 0)


def main():
    # print get_divisors(28)
    # print zip(iter_triangle_numbers(), range(7))[-1]
    first = (x for x in iter_triangle_numbers() if length(get_divisors(x)) > 500).next()
    print get_divisors(first)
    print first
    # print zip(range(500), iter_triangle_numbers())[-1]
    # print get_divisors4(28)


if __name__ == "__main__":
    main()