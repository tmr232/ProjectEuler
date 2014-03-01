from string import ascii_uppercase
from itertools import count
from utils import triangle_number

encode_table = dict(zip(ascii_uppercase, count(1)))



def encode_word(word):
    return sum(encode_table[c] for c in word)


def main():
    triangle_numbers = {triangle_number(n) for n in range(1000)}
    with open("words.txt") as f:
        text = f.read()
    words = (word.strip('"') for word in text.split(","))
    print encode_table['S']
    print encode_word("SKY")
    print sum(1 for word in words if encode_word(word) in triangle_numbers)

if __name__ == "__main__":
    main()