def file_to_list(file):
    with open(file, "r") as text_wrapper:
        lijst = [line.replace('\n', '') for line in text_wrapper]
    return lijst


def code1(file):
    lijst = [i.split('|') for i in file_to_list(file)]

    lijst = [i[1].split(' ') for i in lijst]

    accepted_lengths = (2, 4, 3, 7)
    som = 0
    for i in lijst:
        for j in i:
            if len(j) in accepted_lengths:
                som += 1
    return som


def code2(file):
    global number_display
    lijst = [i.split('|') for i in file_to_list(file)]

    number_display = {0: 'abcefg',
                      1: 'cf',
                      2: 'acdeg',
                      3: 'acdfg',
                      4: 'bcdf',
                      5: 'abdfg',
                      6: 'abdefg',
                      7: 'acf',
                      8: 'abcdefg',
                      9: 'abcdfg'
                      }

    line = 0
    while line < len(lijst):
        for j in range(2):
            lijst[line][j] = ["".join(sorted(k)) for k in lijst[line][j].split(' ') if k]

        line += 1

    easy_lengths = {2: 1,
                    4: 4,
                    3: 7,
                    7: 8}

    for line in lijst:
        map_to_display = {}

        for code in line[0]:
            if len(code) in easy_lengths.keys():
                map_to_display = make_mapping(easy_lengths[len(code)], code, map_to_display)
        print(map_to_display)

    for line in lijst:
        print(line)

    return 'Not solved yet'


def make_mapping(number: int, code: str, map_to_display: dict) -> dict:
    global number_display
    for charIndex in range(len(code)):
        map_to_display[code[charIndex]] = number_display[number][charIndex]
    return map_to_display


if __name__ == '__main__':
    print(f'Answer 1 is: {code1("input.txt")}')
    print(f'Answer 2 is: {code2("test_input.txt")}')
