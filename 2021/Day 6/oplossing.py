
def code1(file):
    lijst = [int(i) for i in fileToList(file)[0].split(',')]

    for i in range(80):
        simulateDay(lijst)

    return len(lijst)


def simulateDay(vissen):
    highValue = len(vissen)
    i = 0
    while i < highValue:
        if vissen[i] == 0:
            vissen.append(8)
            vissen[i] = 6
        else:
            vissen[i] -= 1
        i += 1

    return vissen


def fileToList(file):
    textWrapper = open(file, "r")
    lijst = [line.replace("\n", "") for line in textWrapper]
    textWrapper.close()
    return lijst


def code2(file):
    lijst = [int(i) for i in fileToList(file)[0].split(',')]

    aantallen = [lijst.count(i) for i in range(9)]

    for i in range(256):
        aantallen = betterSimulateDay(aantallen)

    return sum(aantallen)


def betterSimulateDay(aantallen):
    newAantallen = [0] * 9
    for i in range(9):
        if i == 0:
            newAantallen[8] = aantallen[0]
            newAantallen[6] = aantallen[0]
        else:
            newAantallen[i - 1] += aantallen[i]

    return newAantallen


if __name__ == '__main__':
    print(f'Answer 1 is: {code1("input.txt")}')
    print(f'Answer 2 is: {code2("input.txt")}')
