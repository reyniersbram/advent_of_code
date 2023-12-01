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
    >>> get_outer_digits("two1nine")
    (2, 9)
    >>> get_outer_digits("eightwothree")
    (8, 3)
    >>> get_outer_digits("abcone2threexyz")
    (1, 3)
    >>> get_outer_digits("xtwone3four")
    (2, 4)
    >>> get_outer_digits("4nineeightseven2")
    (4, 2)
    >>> get_outer_digits("zoneight234")
    (1, 4)
    >>> get_outer_digits("7pqrstsixteen")
    (7, 6)
    >>> get_outer_digits("one")
    (1, 1)
    """
    digit_line = substitute_digit_strings(line)
    result = (-1, -1)
    for char in digit_line:
        if char.isdigit():
            digit = int(char)
            result = (
                digit if result[0] == -1 else result[0],
                digit
            )
    return result

def substitute_digit_strings(string: str) -> str:
    text_digits = [
        "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"
    ]
    result = string
    for i, v in enumerate(text_digits):
        result = result.replace(v, f"{v}{i + 1}{v}")
    return result


def main(file_name: str):
    """
    >>> main(f"{script_directory}/test1.txt")
    142
    >>> main(f"{script_directory}/test2.txt")
    281
    """
    with open(file_name, 'r') as file:
        lines = [line.replace("\n", "") for line in file]
        print(solve(lines))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main(f"{script_directory}/input.txt")
