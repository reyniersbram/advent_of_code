def file_to_list(file):
    with open(file, "r") as text_wrapper:
        lijst = [line.replace("\n", "") for line in text_wrapper]
    return lijst


def calculate_points(other: str, me: str) -> int:
    wins = {"A": "B",
            "B": "C",
            "C": "A"}
    weights = {"A": 1,
               "B": 2,
               "C": 3}

    if other == me:
        return 3 + weights[me]
    if me == wins[other]:
        return 6 + weights[me]
    return 0 + weights[me]


def part1(file):
    plays = [line.replace("X", "A").replace("Y", "B").replace("Z", "C").split(" ") for line in file_to_list(file)]
    return sum([calculate_points(play[0], play[1]) for play in plays])


def part2(file):
    plays = [line.split(" ") for line in file_to_list(file)]
    points = {"X": 0,
              "Y": 3,
              "Z": 6}
    game_points = sum([points[play[1]] for play in plays])
    weights = {"A": 1,
               "B": 2,
               "C": 3}
    play_points = 0
    for play in plays:
        other, me = play[0], play[1]
        if me == "X":
            mapping = {"A": "C",
                       "B": "A",
                       "C": "B"}
            play_points += weights[mapping[other]]
        elif me == "Y":
            play_points += weights[other]
        else:
            mapping = {"A": "B",
                       "B": "C",
                       "C": "A"}
            play_points += weights[mapping[other]]
    return game_points + play_points


if __name__ == '__main__':
    print(f'Answer 1 is: {part1("input.txt")}')
    print(f'Answer 2 is: {part2("input.txt")}')
