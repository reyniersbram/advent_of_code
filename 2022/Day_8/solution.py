def part1(lines: list[str]):
    rows = [[int(tree) for tree in line] for line in lines]
    columns = [[rows[row_index][column_index] for row_index in range(len(rows))] for column_index in
               range(len(rows[0]))]

    visible_trees = 0
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            visible_trees += not (any(map(lambda a: a >= rows[i][j], rows[i][:j]))
                                  and any(map(lambda a: a >= rows[i][j], rows[i][j + 1:]))
                                  and any(map(lambda a: a >= columns[j][i], columns[j][:i]))
                                  and any(map(lambda a: a >= columns[j][i], columns[j][i + 1:])))
    return visible_trees


def part2(lines: list[str]):
    rows = [[int(tree) for tree in line] for line in lines]
    columns = [[rows[row_index][column_index] for row_index in range(len(rows))] for column_index in
               range(len(rows[0]))]

    max_score = 0
    for i in range(1, len(rows) - 1):
        for j in range(1, len(rows[0]) - 1):
            max_score = max(max_score, calculate_scenic_score((i, j), rows, columns))

    return max_score


def calculate_scenic_score(location: tuple[int, int], rows: list[list[int]], columns: list[list[int]]) -> int:
    i, j = location
    left = 0
    for tree in rows[i][j - 1::-1]:
        left += 1
        if tree >= rows[i][j]:
            break
    right = 0
    for tree in rows[i][j + 1:]:
        right += 1
        if tree >= rows[i][j]:
            break
    up = 0
    for tree in columns[j][i - 1::-1]:
        up += 1
        if tree >= columns[j][i]:
            break
    down = 0
    for tree in columns[j][i + 1:]:
        down += 1
        if tree >= columns[j][i]:
            break
    return left * right * up * down


if __name__ == '__main__':
    file_name = "input.txt"
    with open(file_name, 'r') as text_wrapper:
        file_lines = [line.replace("\n", "") for line in text_wrapper]
        print(f'Answer 1 is: {part1(file_lines)}')
        print(f'Answer 2 is: {part2(file_lines)}')
