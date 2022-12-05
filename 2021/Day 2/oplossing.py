
def fileToList(file):
    textWrapper = open(file, "r")
    lijst = [line for line in textWrapper]
    textWrapper.close()
    return lijst


def dive1(file):
    global horizontal, depth

    lijst = fileToList(file)
    horizontal = 0
    depth = 0

    def forward(x):
        global horizontal
        horizontal += x

    def down(x):
        global depth
        depth += x

    def up(x):
        global depth
        depth -= x

    commands = {"forward": forward,
                "down": down,
                "up": up}

    for line in lijst:
        line = line.replace('\n', '').split(" ")
        commands[line[0]](int(line[1]))

    return horizontal * depth


def dive2(file):
    global horizontal, depth, aim

    lijst = fileToList(file)
    horizontal = 0
    depth = 0
    aim = 0

    def forward(x):
        global horizontal, depth, aim
        horizontal += x
        depth += aim * x

    def down(x):
        global aim
        aim += x

    def up(x):
        global aim
        aim -= x

    commands = {"forward": forward,
                "down": down,
                "up": up}

    for line in lijst:
        line = line.replace('\n', '').split(" ")
        commands[line[0]](int(line[1]))

    return horizontal * depth


if __name__ == '__main__':
    print(f'Answer of 1 is: {dive1("input.txt")}')
    print(f'Answer of 2 is: {dive2("input.txt")}')
