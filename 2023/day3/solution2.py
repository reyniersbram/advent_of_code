#! /usr/bin/env python3

import os
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))


def solve(lines: list[str]) -> int:
    ratio_sum = 0
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "*":
                ratio_sum += get_ratio(row, col, lines)
    return ratio_sum


def get_ratio(row: int, col: int, lines: list[str]) -> int:
    has_top_part = False
    has_NW = False
    has_N  = False
    has_NE = False
    if row > 0:
        if col > 0:
            has_NW = lines[row - 1][col - 1].isdigit()
        has_N = lines[row - 1][col].isdigit()
        if col < len(lines[row - 1]) - 1:
            has_NE = lines[row - 1][col + 1].isdigit()

    if not any([has_NW, has_N, has_NE]):
        has_top_part = 0
    elif has_NW and not has_N and has_NE:
        has_top_part = 2
    else:
        has_top_part = 1

    has_bottom_part = False
    has_SW = False
    has_S  = False
    has_SE = False
    if row < len(lines) - 1:
        if col > 0:
            has_SW = lines[row + 1][col - 1].isdigit()
        has_S = lines[row + 1][col].isdigit()
        if col < len(lines[row + 1]) - 1:
            has_SE = lines[row + 1][col + 1].isdigit()

    if not any([has_SW, has_S, has_SE]):
        has_bottom_part = 0
    elif has_SW and not has_S and has_SE:
        has_bottom_part = 2
    else:
        has_bottom_part = 1

    has_left_part = False
    if col > 0:
        has_left_part = lines[row][col - 1].isdigit()

    has_right_part = False
    if col < len(lines[row]):
        has_right_part = lines[row][col + 1].isdigit()

    if sum([has_top_part, has_bottom_part, has_left_part, has_right_part]) != 2:
        return 0

    top_part_L = 1
    top_part_R = 1
    if has_NW and not has_N and has_NE:
        i = -1
        part_string = ""
        while col + i >= 0 and lines[row - 1][col + i].isdigit():
            part_string = lines[row - 1][col + i] + part_string
            i -= 1
        top_part_L = int(part_string)
        i = 1
        part_string = ""
        while col + i < len(lines[row - 1]) and lines[row - 1][col + i].isdigit():
            part_string += lines[row - 1][col + i]
            i += 1
        top_part_R = int(part_string)
    elif has_NW:
        i = -1
        part_string = ""
        while col + i >= 0 and lines[row - 1][col + i].isdigit():
            part_string = lines[row - 1][col + i] + part_string
            i -= 1
        i = 0
        while col + i < len(lines[row - 1]) and lines[row - 1][col + i].isdigit():
            part_string += lines[row - 1][col + i]
            i += 1
        top_part_L = int(part_string)
    elif has_N:
        part_string = ""
        i = 0
        while col + i < len(lines[row - 1]) and lines[row - 1][col + i].isdigit():
            part_string += lines[row - 1][col + i]
            i += 1
        top_part_L = int(part_string)
    elif has_NE:
        part_string = ""
        i = 1
        while col + i < len(lines[row - 1]) and lines[row - 1][col + i].isdigit():
            part_string += lines[row - 1][col + i]
            i += 1
        top_part_L = int(part_string)


    bottom_part_L = 1
    bottom_part_R = 1
    if has_SW and not has_S and has_SE:
        i = -1
        part_string = ""
        while col + i >= 0 and lines[row + 1][col + i].isdigit():
            part_string = lines[row + 1][col + i] + part_string
            i -= 1
        bottom_part_L = int(part_string)
        i = 1
        part_string = ""
        while col + i < len(lines[row + 1]) and lines[row + 1][col + i].isdigit():
            part_string += lines[row + 1][col + i]
            i += 1
        bottom_part_R = int(part_string)
    elif has_SW:
        i = -1
        part_string = ""
        while col + i >= 0 and lines[row + 1][col + i].isdigit():
            part_string = lines[row + 1][col + i] + part_string
            i -= 1
        i = 0
        while col + i < len(lines[row + 1]) and lines[row + 1][col + i].isdigit():
            part_string += lines[row + 1][col + i]
            i += 1
        bottom_part_L = int(part_string)
    elif has_S:
        part_string = ""
        i = 0
        while col + i < len(lines[row + 1]) and lines[row + 1][col + i].isdigit():
            part_string += lines[row + 1][col + i]
            i += 1
        bottom_part_L = int(part_string)
    elif has_SE:
        part_string = ""
        i = 1
        while col + i < len(lines[row + 1]) and lines[row + 1][col + i].isdigit():
            part_string += lines[row + 1][col + i]
            i += 1
        bottom_part_L = int(part_string)


    left_part = 1
    if has_left_part:
        i = -1
        part_string = ""
        while col + i >= 0 and lines[row][col + i].isdigit():
            part_string = lines[row][col + i] + part_string
            i -= 1
        left_part = int(part_string)

    right_part = 1
    if has_right_part:
        i = 1
        part_string = ""
        while col + i < len(lines[row]) and lines[row][col + i].isdigit():
            part_string += lines[row][col + i]
            i += 1
        right_part = int(part_string)

    return top_part_L * top_part_R * bottom_part_L * bottom_part_R * left_part * right_part


def main(file_name: str):
    """
    >>> main(f"{script_directory}/test.txt")
    467835
    """
    with open(file_name, 'r') as file:
        lines = [line.replace("\n", "") for line in file]
        print(solve(lines))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main(f"{script_directory}/input.txt")
