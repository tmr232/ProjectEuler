def is_double_palindrom(n):
    decimal = "%d" % (n)
    binary = bin(n)[2:]
    return decimal == decimal[::-1] and binary == binary[::-1]

def main():
    print sum(x for x in range(1000000) if is_double_palindrom(x))

if __name__ == "__main__":
    main()