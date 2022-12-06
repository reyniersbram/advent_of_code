from file_reader import file_to_list


def is_marker(buffer: str, length: int) -> bool:
    return len(buffer) == length and len(set(buffer)) == length


def find_marker(input_stream: str, marker_length: int) -> int:
    buffer = input_stream[:marker_length]
    i = marker_length
    while not is_marker(buffer, marker_length):
        buffer = buffer[1::] + input_stream[i]
        i += 1
    return i


def part1(file):
    lijst = file_to_list(file)
    return find_marker(lijst[0], 4)


def part2(file):
    lijst = file_to_list(file)
    return find_marker(lijst[0], 14)


if __name__ == '__main__':
    print(f'Answer 1 is: {part1("input.txt")}')
    print(f'Answer 2 is: {part2("input.txt")}')
