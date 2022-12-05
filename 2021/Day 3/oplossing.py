
def fileToList(file):
    textWrapper = open(file, "r")
    lijst = [line.replace("\n", "") for line in textWrapper]
    textWrapper.close()
    return lijst


def power_consumption(file):
    lijst = fileToList(file)
    gamma = ""
    for i in range(len(lijst[0])):
        zeroCounter = 0
        for line in lijst:
            zeroCounter += 1 if line[i] == "0" else 0
        gamma += "0" if zeroCounter > len(lijst) / 2 else "1"
    epsilon = gamma.replace("1", "2").replace("0", "1").replace("2", "0")
    return int(gamma, 2) * int(epsilon, 2)


def life_support_rating(file):
    lijst = fileToList(file)
    oRating = removeWrongs(lijst)
    coRating = removeWrongs(lijst, False)

    return int(oRating[0], 2) * int(coRating[0], 2)


def removeWrongs(lijst, rating=True):
    i = 0
    ratingLijst = lijst.copy()
    while len(ratingLijst) > 1 and i < len(lijst[0]):
        most = mostCommon([line[i] for line in ratingLijst])
        if most == "2":
            if rating:
                most = "1"
            else:
                most = "0"
        elif not rating:
            most = str(int(not bool(int(most))))
        j = 0
        while j < len(ratingLijst) and len(ratingLijst) > 1:
            if ratingLijst[j][i] == most:
                ratingLijst.remove(ratingLijst[j])
            else:
                j += 1

        i += 1
    return ratingLijst


def mostCommon(lijst):
    zeroCounter = 0
    for line in lijst:
        zeroCounter += 1 if line == "0" else 0

    if zeroCounter > len(lijst) / 2:
        return "0"
    elif zeroCounter == len(lijst)/2:
        return "2"
    else:
        return "1"


if __name__ == '__main__':
    print(f'Answer 1 is: {power_consumption("input.txt")}')
    print(f'Answer 2 is: {life_support_rating("input.txt")}')
