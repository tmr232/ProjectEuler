from itertools import count, takewhile, combinations_with_replacement

from utils import get_proper_divisors, take


MAX = 28123+10




def is_abundant(number):
    return sum(get_proper_divisors(number)) > number

def iter_abundant_numbers():
    return (n for n in count() if is_abundant(n))

def main():
    print take(10, iter_abundant_numbers())
    # print len(list(takewhile(lambda n: n < MAX, iter_abundant_numbers())))
    table = {sum(x) for x in combinations_with_replacement(takewhile(lambda x: x <= MAX / 2, iter_abundant_numbers()), 2)}
    print "Got table"
    print sum(x for x in range(MAX) if x not in table)

if __name__ == "__main__":
    main()