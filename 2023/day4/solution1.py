#! /usr/bin/env python3

import re
import os
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))


def solve(lines: list[str]) -> int:
    card_sum = 0
    for line in lines:
        card_sum += get_card_points(line)
    return card_sum

def num_of_winning_numbers(card: str) -> int:
    card = re.sub(r"Card +\d+: ", "", card)
    winning, got = ([int(x) for x in numbers.split(" ") if x != ""] for numbers in card.split("|"))
    return len([x for x in got if x in winning])

def get_card_points(card: str) -> int:
    winning_numbers = num_of_winning_numbers(card)
    return 2 ** (winning_numbers - 1) if winning_numbers >= 2 else winning_numbers


def main(file_name: str):
    """
    >>> main(f"{script_directory}/test.txt")
    13
    """
    with open(file_name, 'r') as file:
        lines = [line.replace("\n", "") for line in file]
        print(solve(lines))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main(f"{script_directory}/input.txt")
