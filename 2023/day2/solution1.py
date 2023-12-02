#! /usr/bin/env python3

from __future__ import annotations
import re
import os
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))


class CubeSet:
    def __init__(self, red: int, green: int, blue: int) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self) -> str:
        return f"red: {self.red}, green: {self.green}, blue: {self.blue}"

    def is_possible(self, other: CubeSet) -> bool:
        return self.red <= other.red and self.green <= other.green and self.blue <= other.blue

    @property
    def power(self) -> int:
        return self.red * self.green * self.blue
    

class Game:
    def __init__(self, line: str) -> None:
        line = line.replace(" ", "")
        game_id_string, revealed_cubes_string = line.split(":")
        cube_set_strings = revealed_cubes_string.split(";")

        cube_sets = []
        for cube_set_string in cube_set_strings:
            pairs = re.findall(r"(\d+)([a-z]+)", cube_set_string)
            colors = {pair[1]: int(pair[0]) for pair in pairs}
            cube_sets.append(CubeSet(colors.get("red", 0), colors.get("green", 0), colors.get("blue", 0)))

        self.id = int(game_id_string.replace("Game", ""))
        self.cube_sets = cube_sets

    def __str__(self) -> str:
        return f"Game {self.id}: \n{[str(cube_set) for cube_set in self.cube_sets]}"

    def is_possible(self, other_cube_set: CubeSet) -> bool:
        return all([cube_set.is_possible(other_cube_set) for cube_set in self.cube_sets])

def solve(lines: list[str]) -> int:
    possible_sum = 0
    for line in lines:
        game = Game(line)
        if game.is_possible(CubeSet(12, 13, 14)):
            possible_sum += game.id
    return possible_sum


def main(file_name: str):
    """
    >>> main(f"{script_directory}/test.txt")
    8
    """
    with open(file_name, 'r') as file:
        lines = [line.replace("\n", "") for line in file]
        print(solve(lines))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main(f"{script_directory}/input.txt")
