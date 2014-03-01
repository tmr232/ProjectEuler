from utils import get_prime_divisors, take
from itertools import count

def main():
    four_divisors = (x for x in count(2*3*5*7) if len(set(get_prime_divisors(x))) == 4)

    a = four_divisors.next()
    b = four_divisors.next()
    c = four_divisors.next()
    d = four_divisors.next()

    while 1:
        a, b, c, d = b, c, d, four_divisors.next()
        if a + 3 == b + 2 == c + 1 == d:
            break

    print a, b, c ,d

    print get_prime_divisors(a)



if __name__ == "__main__":
    main()