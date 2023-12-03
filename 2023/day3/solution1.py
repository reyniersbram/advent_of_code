#! /usr/bin/env python3

import os
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))


def solve(lines: list[str]) -> int:
    part_sum = 0
    for row, line in enumerate(lines):
        adjacent_to_symbol = False
        part_number_string = ""
        for col, char in enumerate(line):
            if char.isdigit():
                part_number_string += char
                adjacent_to_symbol |= check_adjacent(row, col, lines)
            else:
                if adjacent_to_symbol:
                    part_sum += int(part_number_string)
                    adjacent_to_symbol = False
                part_number_string = ""
    return part_sum


def check_adjacent(row: int, col: int, lines: list[str]) -> bool:
    has_adjacent_symbol = False
    i = -1
    while not has_adjacent_symbol and i < 2:
        if row + i >= 0 and row + i < len(lines):
            j = -1
            while not has_adjacent_symbol and j < 2:
                if col + j >= 0 and col + j < len(lines[row + i]):
                    char = lines[row + i][col + j]
                    has_adjacent_symbol |= (char != "." and char != "\n" and not char.isdigit())
                j += 1
        i += 1
    return has_adjacent_symbol


def main(file_name: str):
    """
    >>> main(f"{script_directory}/test.txt")
    4361
    """
    with open(file_name, 'r') as file:
        lines = [line for line in file]
        print(solve(lines))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main(f"{script_directory}/input.txt")
