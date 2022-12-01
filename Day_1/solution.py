def file_to_list(file):
    with open(file, "r") as text_wrapper:
        lijst = [line.replace("\n", "") for line in text_wrapper]
    return lijst


def part1(file):
    lijst = file_to_list(file)
    max_cal = 0
    current_elf_cals = 0
    for line in lijst:
        if line != "":
            current_elf_cals += int(line)
        else:
            max_cal = max(max_cal, current_elf_cals)
            current_elf_cals = 0
    return max_cal


def part2(file):
    lijst = file_to_list(file)
    max_cals = [0, 0, 0]
    current_elf_cals = 0
    for line in lijst:
        if line != "":
            current_elf_cals += int(line)
        else:
            for i in range(3):
                max_cals[i], current_elf_cals = max(max_cals[i], current_elf_cals), min(max_cals[i], current_elf_cals)
            current_elf_cals = 0
    return sum(max_cals)


if __name__ == '__main__':
    print(f'Answer 1 is: {part1("input.txt")}')
    print(f'Answer 2 is: {part2("input.txt")}')
