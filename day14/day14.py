from copy import deepcopy


def simulate(cave, start):
    outside = False

    sandCountAtRest = 0

    while not outside:
        current = start

        atRest = False

        while not atRest and not outside:
            new = (current[0], current[1] + 1)

            if new in cave:
                left = (current[0] - 1, current[1] + 1)
                if left not in cave:
                    current = left
                else:
                    right = (current[0] + 1, current[1] + 1)
                    if right not in cave:
                        current = right
                    else:
                        atRest = True
                        cave[current] = "o"
                        sandCountAtRest += 1
            else:
                current = new

            if current[1] > maxY:
                outside = True

            if current == start:
                outside = True

    return sandCountAtRest


f = open("input.txt", "r")

cave = {}
minX = 1000
maxX = 0
minY = 1000
maxY = 0

for line in f:
    trimmedLine = line.strip()
    split = trimmedLine.split(" -> ")

    previous = None
    for s in split:
        pair = s.split(",")
        current = (int(pair[0]), int(pair[1]))
        minX = min(minX, current[0])
        maxX = max(maxX, current[0])
        minY = min(minY, current[1])
        maxY = max(maxY, current[1])

        if previous is None:
            previous = current
            cave[current] = "#"
        else:
            if previous[0] == current[0]:
                r = range(previous[1], current[1] + 1) if current[1] >= previous[1] else range(
                    previous[1], current[1] - 1, -1)
                for y in r:
                    pos = (previous[0], y)
                    cave[pos] = "#"
            else:
                r = range(previous[0], current[0] + 1) if current[0] >= previous[0] else range(
                    previous[0], current[0] - 1, -1)
                for x in r:
                    pos = (x, previous[1])
                    cave[pos] = "#"
            previous = current

f.close()

start = (500, 0)
cave[start] = "+"

minX = min(minX, start[0])
maxX = max(maxX, start[0])
minY = min(minY, start[1])
maxY = max(maxY, start[1])

sandCountAtRest = simulate(deepcopy(cave), start)

print(f"Part 1 answer: {sandCountAtRest}")

maxY += 2

minX -= 10000
maxX += 10000

for x in range(minX, maxX + 1):
    pos = (x, maxY)
    cave[pos] = "#"

sandCountAtRest = simulate(deepcopy(cave), start)

print(f"Part 2 answer: {sandCountAtRest}")
