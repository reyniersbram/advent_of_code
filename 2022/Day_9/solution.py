import math


def part1(lines: list[str]):
    visited_positions = set()
    head = tail = (0, 0)
    for line in lines:
        line = line.split()
        for _ in range(int(line[1])):
            head, tail = do_step(line[0], head, tail)
            visited_positions.add(tail)

    return len(visited_positions)


def part2(lines: list[str]):
    return "Not solved yet"


def do_step(direction: [str], head: tuple[int, int], tail: [int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    move_head = {
        'R': lambda x, y: (x + 1, y),
        'L': lambda x, y: (x - 1, y),
        'U': lambda x, y: (x, y + 1),
        'D': lambda x, y: (x, y - 1)
    }
    map_tail_movement = lambda x: 0 if x == 0 else abs(x) - 1  # NOQA E731

    head = move_head[direction](*head)
    x_distance, y_distance = head[0] - tail[0], head[1] - tail[1]
    if abs(x_distance) >= 2:
        tail = (tail[0] + (x_distance // 2), tail[1] + y_distance)
    elif abs(y_distance) >= 2:
        tail = (tail[0] + x_distance, tail[1] + (y_distance // 2))
    else:
        tail = (tail[0] + map_tail_movement(x_distance), tail[1] + map_tail_movement(y_distance))
    return head, tail


if __name__ == '__main__':
    file_name = "input.txt"
    with open(file_name, 'r') as text_wrapper:
        file_lines = [line.replace("\n", "") for line in text_wrapper]
        print(f'Answer 1 is: {part1(file_lines)}')
        print(f'Answer 2 is: {part2(file_lines)}')
