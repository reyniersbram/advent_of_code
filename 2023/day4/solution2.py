#! /usr/bin/env python3

import re
import os
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))


def solve(lines: list[str]) -> int:
    card_copies = [1] * len(lines) # start with 1 copy of each card
    for i, line in enumerate(lines):
        winning_numbers = num_of_winning_numbers(line)
        for j in range(1, winning_numbers + 1):
            card_copies[i + j] += card_copies[i]
    return sum(card_copies)

def num_of_winning_numbers(card: str) -> int:
    card = re.sub(r"Card +\d+: ", "", card)
    winning, got = ([int(x) for x in numbers.split(" ") if x != ""] for numbers in card.split("|"))
    return len([x for x in got if x in winning])


def main(file_name: str):
    """
    >>> main(f"{script_directory}/test.txt")
    30
    """
    with open(file_name, 'r') as file:
        lines = [line.replace("\n", "") for line in file]
        print(solve(lines))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main(f"{script_directory}/input.txt")
