import statistics


def code1(file):
    lijst = [int(i) for i in fileToList(file)[0].split(',')]
    mediaan = statistics.median(lijst)
    som = 0
    for i in lijst:
        som += abs(i - mediaan)

    return int(som)


def fileToList(file):
    textWrapper = open(file, "r")
    lijst = [line.replace("\n", "") for line in textWrapper]
    textWrapper.close()
    return lijst


def code2(file):
    lijst = [int(i) for i in fileToList(file)[0].split(',')]
    gemiddelde = round(statistics.mean(lijst))
    print(gemiddelde)
    print(statistics.mean(lijst))
    som = 0
    for i in lijst:
        som += sum(range(abs(i - gemiddelde) + 1))

    return int(som)


if __name__ == '__main__':
    print(f'Answer 1 is: {code1("input.txt")}')
    print(f'Answer 2 is: {code2("input.txt")}')
