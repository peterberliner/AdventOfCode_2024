import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def openone(input):
    lines = []
    with open(os.path.join(__location__, input)) as input:
        for line in input:
            lines.append(line.strip("\n"))

    list_a: list[int] = []
    list_b: list[int] = []
    for line in lines:
        chunks = line.split()
        list_a.append(int(chunks[0]))
        list_b.append(int(chunks[1]))

    return (list_a, list_b)


def calculate_total_distance(list_a: list[int], list_b: list[int]):
    list_a.sort()
    list_b.sort()

    dif = 0

    for i in range(len(list_a)):
        dif += abs(list_a[i] - list_b[i])

    return dif
