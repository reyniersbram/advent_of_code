from file_reader import file_to_list


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if len(self.items) > 0 else None


def parse_moves(stacks: list[Stack], moves: list[str]) -> None:
    moves = [tuple(int(i) for i in move.split(' ')[1::2]) for move in moves]
    for move in moves:
        for i in range(move[0]):
            stacks[move[2] - 1].push(stacks[move[1] - 1].pop())


def parse_moves_multiple(stacks: list[Stack], moves: list[str]) -> None:
    moves = [tuple(int(i) for i in move.split(' ')[1::2]) for move in moves]
    for move in moves:
        crates = []
        for i in range(move[0]):
            crates.append(stacks[move[1] - 1].pop())
        crates.reverse()
        for crate in crates:
            stacks[move[2] - 1].push(crate)


def parse_stacks(input_lines: list[str]) -> list[Stack]:
    num_of_stacks = len(input_lines.pop().split())
    stacks = [Stack() for _ in range(num_of_stacks)]
    input_lines.reverse()
    input_lines = [line[1::4] for line in input_lines]
    for line in input_lines:
        for i in range(num_of_stacks):
            if len(line) <= i:
                pass
            elif line[i] == ' ':
                pass
            else:
                stacks[i].push(line[i])
    return stacks


def part1(file):
    lijst = file_to_list(file)
    stacks_input = lijst[:lijst.index('')]
    moves = lijst[lijst.index('') + 1:]
    stacks = parse_stacks(stacks_input)
    parse_moves(stacks, moves)
    return ''.join(stack.peek() for stack in stacks)


def part2(file):
    lijst = file_to_list(file)
    stacks_input = lijst[:lijst.index('')]
    moves = lijst[lijst.index('') + 1:]
    stacks = parse_stacks(stacks_input)
    parse_moves_multiple(stacks, moves)
    return ''.join(stack.peek() for stack in stacks)


if __name__ == '__main__':
    print(f'Answer 1 is: {part1("input.txt")}')
    print(f'Answer 2 is: {part2("input.txt")}')
