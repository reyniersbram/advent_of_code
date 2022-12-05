import re


def fileToList(file):
    textWrapper = open(file, "r")
    lijst = [line.replace("\n", "") for line in textWrapper]
    textWrapper.close()
    return lijst


def score1(file):
    lijst = fileToList(file)
    numbers = [number for number in lijst[0].split(",")]
    lijst.remove(lijst[0])
    lijst.remove(lijst[0])

    velden = inputToList(lijst)

    for number in numbers:
        velden = shoutNumber(velden, number)
        for veld in velden:
            check = checkBingo(veld)
            if check:
                som = 0
                for line in veld:
                    for i in line:
                        som += int(i)
                return som * int(number)


def shoutNumber(velden, number):
    for veld in velden:
        for line in veld:
            try:
                line[line.index(number)] = False
            except ValueError:
                pass

    return velden


def checkBingo(veld):
    for line in veld:
        if line == [False, False, False, False, False]:
            return True
    for i in range(len(veld)):
        checker = True
        for line in veld:
            checker *= bool(line[i]) is False
        if checker:
            return True

    return False


def inputToList(lijst):
    velden = []

    index = 0
    while index < len(lijst):
        velden.append([re.sub('\s\s', ' ', re.sub('^\s', '', lijst[index + i])).split(" ") for i in range(5)])
        index += 6

    return velden


def score2(file):
    lijst = fileToList(file)

    numbers = lijst[0].split(",")
    lijst.remove(lijst[0])
    lijst.remove(lijst[0])

    velden = inputToList(lijst)

    for number in numbers:
        velden = shoutNumber(velden, number)
        for veld in velden:
            check = checkBingo(veld)
            if check:
                if len(velden) == 1:
                    som = 0
                    for line in veld:
                        for i in line:
                            som += int(i)
                    return som * int(number)
                velden.remove(veld)


if __name__ == '__main__':
    print(f'Answer 1 is: {score1("input.txt")}')
    print(f'Answer 2 is: {score2("input.txt")}')
