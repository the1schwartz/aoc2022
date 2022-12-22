import sys


def beaconCannotBePresentSum(sensorsWithClosestBeacon, map, y, minX, maxX):
    beaconCannotBePresentSum = 0

    for x in range(minX, maxX + 1):
        pos = (x, y)
        for entry in sensorsWithClosestBeacon:
            manhattanDistance = abs(
                entry[0][0] - pos[0]) + abs(entry[0][1] - pos[1])
            if manhattanDistance <= entry[2] and pos not in map:
                beaconCannotBePresentSum += 1
                break

    return beaconCannotBePresentSum


def possibleBeaonPositions(sensorsWithClosestBeacon, map, y, minX, maxX):
    result = []

    x = minX
    while x <= maxX:
        pos = (x, y)
        possiblePosition = True

        for entry in sensorsWithClosestBeacon:
            sensor = entry[0]
            manhattanDistance = abs(
                sensor[0] - pos[0]) + abs(sensor[1] - pos[1])
            dist = entry[2]
            possiblePosition = possiblePosition and manhattanDistance > dist and pos not in map

            if not possiblePosition:
                break

        if possiblePosition:
            result.append(pos)
        else:
            for entry in sensorsWithClosestBeacon:
                sensor = entry[0]
                manhattanDistance = abs(
                    sensor[0] - pos[0]) + abs(sensor[1] - pos[1])
                dist = entry[2]
                if manhattanDistance <= dist and pos not in map:
                    xDiff = x - sensor[0]
                    yDiff = y - sensor[1]
                    x += dist - abs(yDiff) - xDiff
                    break

        x += 1

    return result


sensorsWithClosestBeacon = []
minX = sys.maxsize
maxX = -sys.maxsize
minY = sys.maxsize
maxY = -sys.maxsize

map = {}

f = open("input.txt", "r")

for line in f:
    trimmedLine = line.strip()
    split = trimmedLine.split(": ")

    sensorSplit = split[0].replace("Sensor at ", "").split(", ")
    sensor = (int(sensorSplit[0].split("=")[1]),
              int(sensorSplit[1].split("=")[1]))

    beaconSplit = split[1].replace("closest beacon is at ", "").split(", ")
    beacon = (int(beaconSplit[0].split("=")[1]),
              int(beaconSplit[1].split("=")[1]))
    manhattanDistance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

    map[sensor] = "S"
    map[beacon] = "B"

    minX = min(minX, sensor[0] - manhattanDistance)
    maxX = max(maxX, sensor[0] + manhattanDistance)
    minY = min(minY, sensor[1] - manhattanDistance)
    maxY = max(maxY, sensor[1] + manhattanDistance)
    minX = min(minX, beacon[0] - manhattanDistance)
    maxX = max(maxX, beacon[0] + manhattanDistance)
    minY = min(minY, beacon[1] - manhattanDistance)
    maxY = max(maxY, beacon[1] + manhattanDistance)

    sensorsWithClosestBeacon.append((sensor, beacon, manhattanDistance))

f.close()

yLine = 2000000

notPresentSum = beaconCannotBePresentSum(
    sensorsWithClosestBeacon, map, yLine, minX, maxX)

print(f"Part 1 answer: {notPresentSum}")

possiblePositions = []
limit = 4000000

for y in range(limit + 1):
    positions = possibleBeaonPositions(
        sensorsWithClosestBeacon, map, y, 0, limit)

    for p in positions:
        possiblePositions.append(p)

frequency = 4000000 * possiblePositions[0][0] + possiblePositions[0][1]

print(f"Part 2 answer: {frequency}")
