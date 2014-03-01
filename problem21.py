from utils import amicable_numbers










def main():
    print sum({x for x in amicable_numbers(10000)})


if __name__ == "__main__":
    main()