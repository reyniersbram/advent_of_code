from __future__ import annotations

from file_reader import file_to_list
from FileSystem import File, Directory


def parse_file(current_dir: Directory, line: str) -> File:
    file = line.split()
    if file[0] == "dir":
        return Directory(current_dir, file[1])
    return File(current_dir, file[1], int(file[0]))


def part1(input_file):
    lines = file_to_list(input_file)
    root = Directory(None, "/")
    root.root = root
    all_dirs = {root.get_path(): root}
    current_dir = root
    line_index: int = 0
    while line_index < len(lines):
        line = lines[line_index]
        if line[0] == '$':
            command = line.split()[1::]
            if command[0] == "cd":
                current_dir = current_dir.cd(command[1])
                line_index += 1
            else:  # command[0] == "ls"
                line_index += 1
                while line_index < len(lines) and lines[line_index][0] != '$':
                    line = lines[line_index]
                    file = parse_file(current_dir, line)
                    if file.is_dir() and not str(file) in all_dirs:
                        all_dirs[file.get_path()] = file
                    current_dir.add_file(file)
                    line_index += 1
    return sum(directory.get_size() for (_, directory) in all_dirs.items() if directory.get_size() < 100_000)


def part2(input_file):
    lines = file_to_list(input_file)
    root = Directory(None, "/")
    root.root = root
    all_dirs = {root.get_path(): root}
    current_dir = root
    line_index: int = 0
    while line_index < len(lines):
        line = lines[line_index]
        if line[0] == '$':
            command = line.split()[1::]
            if command[0] == "cd":
                current_dir = current_dir.cd(command[1])
                line_index += 1
            else:  # command[0] == "ls"
                line_index += 1
                while line_index < len(lines) and lines[line_index][0] != '$':
                    line = lines[line_index]
                    file = parse_file(current_dir, line)
                    if file.is_dir() and not str(file) in all_dirs:
                        all_dirs[file.get_path()] = file
                    current_dir.add_file(file)
                    line_index += 1

    total_space = 70_000_000
    needed_space = 30_000_000
    available_space = total_space - root.get_size()
    space_to_free = needed_space - available_space

    possible_dirs = (directory.get_size() for (_, directory) in all_dirs.items() if directory.get_size() >= space_to_free)

    return min(possible_dirs)


if __name__ == '__main__':
    print(f'Answer 1 is: {part1("input.txt")}')
    print(f'Answer 2 is: {part2("input.txt")}')
