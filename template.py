from typing import Generator


def part1(lines: Generator[str, None, None]):
    return "Not solved yet"


def part2(lines: Generator[str, None, None]):
    return "Not solved yet"


if __name__ == '__main__':
    file_name = "input.txt"
    with open(file_name,'r') as text_wrapper:  
        lines = (line.replace("\n", "") for line in text_wrapper)
    print(f'Answer 1 is: {part1(lines)}')
    print(f'Answer 2 is: {part2(lines)}')
