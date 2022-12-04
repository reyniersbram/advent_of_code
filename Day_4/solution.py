def file_to_list(file):
    with open(file, "r") as text_wrapper:
        lijst = [line.replace("\n", "") for line in text_wrapper]
    return lijst


def to_set(*start_end):
    return set(range(*start_end))


def part1(file):
    lijst = file_to_list(file)
    sections = ((tuple(int(x) for x in section.split('-')) for section in line.split(',')) for line in lijst)
    sections = (tuple(to_set(section[0], section[1] + 1) for section in pair) for pair in sections)
    sections_overlap = ((pair[0] | pair[1] == pair[0] or pair[0] | pair[1] == pair[1]) for pair in sections)

    return sum(sections_overlap)


def part2(file):
    lijst = file_to_list(file)
    sections = ((tuple(int(x) for x in section.split('-')) for section in line.split(',')) for line in lijst)
    sections = (tuple(to_set(section[0], section[1] + 1) for section in pair) for pair in sections)
    sections_overlap = (len(pair[0] & pair[1]) != 0 for pair in sections)
    return sum(sections_overlap)


if __name__ == '__main__':
    print(f'Answer 1 is: {part1("input.txt")}')
    print(f'Answer 2 is: {part2("input.txt")}')
