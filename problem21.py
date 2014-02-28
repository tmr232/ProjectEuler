from problem12 import get_divisors

def get_proper_divisors(number):
    divisors = get_divisors(number)
    divisors.discard(number)
    return divisors


def sum_proper_divisors(number):
    return sum(get_proper_divisors(number))

def gen_div_sum_table(up_to):
    table = range(up_to)
    for i, n in enumerate(table):
        table[i] = sum_proper_divisors(n)

    return table

def iter_amicable_pairs(up_to):
    table = gen_div_sum_table(up_to)
    for i, n in ((i, n) for i, n in enumerate(table) if n < up_to):
        if table[n] == i:
            yield (i, n)

def amicable_numbers(up_to):
    return (x[0] for x in iter_amicable_pairs(up_to) if x[0] != x[1])

def main():
    print sum({x for x in amicable_numbers(10000)})


if __name__ == "__main__":
    main()