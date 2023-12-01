#! /usr/bin/env python3

import os
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

def solve(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        a, b = get_outer_digits(line)
        sum += 10 * a + b

    return sum


def get_outer_digits(line: str) -> tuple[int, int]:
    """
    >>> get_outer_digits("1abc2")
    (1, 2)
    >>> get_outer_digits("pqr3stu8vwx")
    (3, 8)
    >>> get_outer_digits("a1b2c3d4e5f")
    (1, 5)
    >>> get_outer_digits("treb7uchet")
    (7, 7)
    """
    result = (-1, -1)
    for char in line:
        if char.isdigit():
            digit = int(char)
            result = (
                digit if result[0] == -1 else result[0],
                digit
            )

    return result


def main(file_name: str):
    """
    >>> main(f"{script_directory}/test1.txt")
    142
    """
    with open(file_name, 'r') as file:
        lines = [line.replace("\n", "") for line in file]
        print(solve(lines))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main(f"{script_directory}/input.txt")
