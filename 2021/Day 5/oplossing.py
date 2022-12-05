from timeit import default_timer as timer


def fileToList(file):
    textWrapper = open(file, "r")
    lijst = [line.replace("\n", "") for line in textWrapper]
    textWrapper.close()
    return lijst


def overlap1(file):
    lijst = fileToList(file)
    rangeList = []

    for line in lijst:
        newItem = textToCoords(line)
        if newItem[0][0] == newItem[1][0] or newItem[0][1] == newItem[1][1]:
            rangeList.append(newItem)

    coordList = {}

    for coord in rangeList:
        if coord[0][0] != coord[1][0]:
            coordList = horizontal(coord, coordList)
        else:
            coordList = vertical(coord, coordList)

    return countLines(coordList)


def overlap2(file):
    lijst = fileToList(file)
    rangeList = [textToCoords(line) for line in lijst]

    coordList = {}
    for coord in rangeList:
        if coord[0][0] == coord[1][0] or coord[0][1] == coord[1][1]:
            if coord[0][0] != coord[1][0]:
                coordList = horizontal(coord, coordList)
            else:
                coordList = vertical(coord, coordList)
        else:
            x = min(coord[0][0], coord[1][0])
            highX = max(coord[0][0], coord[1][0])
            m = (coord[0][1] - coord[1][1]) / (coord[0][0] - coord[1][0])

            if m < 0:
                y = max(coord[0][1], coord[1][1])
                highY = min(coord[0][1], coord[1][1])
                while x < highX + 1 and y >= highY:
                    try:
                        coordList[f'{[x, y]}'] += 1
                    except KeyError:
                        coordList[f'{[x, y]}'] = 1
                    x += 1
                    y -= 1
            else:
                y = min(coord[0][1], coord[1][1])
                highY = max(coord[0][1], coord[1][1])
                while x < highX + 1 and y < highY + 1:
                    try:
                        coordList[f'{[x, y]}'] += 1
                    except KeyError:
                        coordList[f'{[x, y]}'] = 1
                    x += 1
                    y += 1


            """m = (coord[0][1] - coord[1][1]) / (coord[0][0] - coord[1][0])
            x1 = coord[0][0]
            y1 = coord[0][1]
            for x in range(lowX, highX + 1):
                for y in range(lowY, highY + 1):
                    if isOnDiagonal(m, x1, y1, x, y):
                        try:
                            coordList[f'{[x, y]}'] += 1
                        except KeyError:
                            coordList[f'{[x, y]}'] = 1"""

    return countLines(coordList)


# returns a list of tuples: the begin-and end-coordinates
def textToCoords(line):
    return [tuple([int(coord) for coord in coords.split(",")]) for coords in line.split(" -> ")]


def vertical(coord, coordList):
    low = min(coord[0][1], coord[1][1])
    high = max(coord[0][1], coord[1][1])
    const = coord[0][0]

    for i in range(low, high + 1):
        try:
            coordList[f'{[const, i]}'] += 1
        except KeyError:
            coordList[f'{[const, i]}'] = 1
    return coordList


def horizontal(coord, coordList):
    low = min(coord[0][0], coord[1][0])
    high = max(coord[0][0], coord[1][0])
    const = coord[0][1]

    for i in range(low, high + 1):
        try:
            coordList[f'{[i, const]}'] += 1
        except KeyError:
            coordList[f'{[i, const]}'] = 1
    return coordList


def countLines(coordList):
    numberOfLines = 0
    for coord, lines in coordList.items():
        if lines != 1:
            numberOfLines += 1
    return numberOfLines


def isOnDiagonal(m, x, y, x1, y1):
    return y - y1 == m * (x - x1)


def overlap3(file):
    lijst = fileToList(file)
    rangeList = [textToCoords(line) for line in lijst]

    coordList = {}
    for coord in rangeList:
        if coord[0][0] == coord[1][0] or coord[0][1] == coord[1][1]:
            if coord[0][0] != coord[1][0]:
                coordList = horizontal(coord, coordList)
            else:
                coordList = vertical(coord, coordList)
        else:
            lowX = min(coord[0][0], coord[1][0])
            highX = max(coord[0][0], coord[1][0])
            m = (coord[0][1] - coord[1][1]) / (coord[0][0] - coord[1][0])
            lowY = min(coord[0][1], coord[1][1])
            highY = max(coord[0][1], coord[1][1])

            m = (coord[0][1] - coord[1][1]) / (coord[0][0] - coord[1][0])
            x1 = coord[0][0]
            y1 = coord[0][1]
            for x in range(lowX, highX + 1):
                for y in range(lowY, highY + 1):
                    if isOnDiagonal(m, x1, y1, x, y):
                        try:
                            coordList[f'{[x, y]}'] += 1
                        except KeyError:
                            coordList[f'{[x, y]}'] = 1

    return countLines(coordList)


if __name__ == '__main__':
    print(f'Answer 1 is: {overlap1("input.txt")}')
    start = timer()
    print(f'Answer 2 is: {overlap2("input.txt")}')
    print(f'With while: {timer() - start}')
    start = timer()
    print(f'Answer 2 is: {overlap3("input.txt")}')
    print(f'With nested for: {timer() - start}')
