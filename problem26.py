def long_division(a, b):
    result = []
    visited = {a}
    while a > 0:
        if a < b:
            a *= 10

        else:
            x = a // b
            a -= x * b
            if a in visited:
                break
            visited.add(a)
            result.append(x)

    return result

def main():
    print long_division(1, 729)
    print max(range(1, 1000), key=lambda x: len(long_division(1, x)))

if __name__ == "__main__":
    main()