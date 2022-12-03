def file_to_list(file):
    with open(file, "r") as text_wrapper:
        lijst = [line.replace("\n", "") for line in text_wrapper]
    return lijst


def part1(file):
    lijst = file_to_list(file)
    common_items = ((set(line[:len(line) // 2]) & set(line[len(line) // 2:])).pop() for line in lijst)
    priority_sum = sum(ord(item) - (ord('a') - 1) if item.islower() else ord(item) - (ord('A') - 27) for item in
                       common_items)
    return priority_sum


def part2(file):
    lijst = file_to_list(file)
    groups = (lijst[i: i + 3] for i in range(0, len(lijst), 3))
    common_items = ((set(group[0]) & set(group[1]) & set(group[2])).pop() for group in groups)
    priority_sum = sum(ord(item) - (ord('a') - 1) if item.islower() else ord(item) - (ord('A') - 27) for item in
                       common_items)
    return priority_sum


if __name__ == '__main__':
    print(f'Answer 1 is: {part1("input.txt")}')
    print(f'Answer 2 is: {part2("input.txt")}')
