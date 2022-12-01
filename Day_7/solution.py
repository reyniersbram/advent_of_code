def file_to_list(file):
    with open(file, "r") as text_wrapper:
        lijst = [line.replace("\n", "") for line in text_wrapper]
    return lijst


def part1(file):
    lijst = file_to_list(file)
    return "Not solved yet"


def part2(file):
    lijst = file_to_list(file)
    return "Not solved yet"


if __name__ == '__main__':
    print(f'Answer 1 is: {part1("input.txt")}')
    print(f'Answer 2 is: {part2("input.txt")}')
