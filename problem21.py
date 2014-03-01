from utils import get_proper_divisors, amicable_numbers


def sum_proper_divisors(number):
    return sum(get_proper_divisors(number))

def gen_div_sum_table(up_to):
    table = range(up_to)
    for i, n in enumerate(table):
        table[i] = sum_proper_divisors(n)

    return table





def main():
    print sum({x for x in amicable_numbers(10000)})


if __name__ == "__main__":
    main()