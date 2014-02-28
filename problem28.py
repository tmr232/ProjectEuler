def sum_spiral_diagonals(size):
    total = 1
    for i in range(3, size + 1, 2):
        total += 4 * (i ** 2) - 6 * (i - 1)
        
    return total


def main():
    print sum_spiral_diagonals(1001)


if __name__ == "__main__":
    main()