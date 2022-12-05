# https://dodona.ugent.be/nl/courses/961/series/10656/activities/325088532

def file_to_list(file):
    text_wrapper = open(file, "r")
    lijst = [line for line in text_wrapper]
    text_wrapper.close()
    return lijst


def sonar1(file):

    lijst = file_to_list(file)
    prev_line = int(lijst[0])
    increases = 0

    for line in lijst:
        if int(line) > prev_line:
            increases += 1
        prev_line = int(line)

    return increases


def sonar2(file):

    lijst = file_to_list(file)
    increases = 0
    prev_line = int(lijst[1]) + int(lijst[0]) + int(lijst[2])

    for i in range(1, len(lijst) - 1):
        som = int(lijst[i]) + int(lijst[i + 1]) + int(lijst[i - 1])
        if som > prev_line:
            increases += 1
        prev_line = som

    return increases


if __name__ == '__main__':
    print(f'Answer of 1 is: {sonar1("input.txt")}')
    print(f'Answer of 2 is: {sonar2("input.txt")}')
