def updateTailPosition(p1: list[int], p2: list[int]):
    result = [p2[0], p2[1]]
    if abs(p1[0] - p2[0]) > 1 or abs(p1[1] - p2[1]) > 1:
        if abs(p1[0] - p2[0]) > 1 and p1[1] == p2[1]:
            result[0] = int((p1[0] + p2[0]) / 2)
        elif abs(p1[0] - p2[0]) > 1 and p1[1] != p2[1]:
            result[0] = int((p1[0] + p2[0]) / 2)
            result[1] = p1[1]
        elif abs(p1[1] - p2[1]) > 1 and p1[0] == p2[0]:
            result[1] = int((p1[1] + p2[1]) / 2)
        elif abs(p1[1] - p2[1]) > 1 and p1[0] != p2[0]:
            result[1] = int((p1[1] + p2[1]) / 2)
            result[0] = p1[0]

    return result


f = open("input.txt", "r")

headPosition = [11, 5]
tailPosition = [11, 5]
knotPositions = []
totalKnots = 10
lastKnotIndex = totalKnots - 1
for i in range(totalKnots):
    knotPositions.append([11, 5])
uniqueTailPositions = set()
uniqueLastKnotPositions = set()

for line in f:
    trimmedLine = line.strip()
    split = trimmedLine.split(" ")

    command = split[0]
    count = int(split[1])

    if command == "R":
        for x in range(count):
            headPosition[0] += 1
            tailPosition = updateTailPosition(headPosition, tailPosition)
            uniqueTailPositions.add((tailPosition[0], tailPosition[1]))

            knotPositions[0][0] = headPosition[0]

            for i in range(lastKnotIndex):
                knotPositions[i+1] = updateTailPosition(
                    knotPositions[i], knotPositions[i+1])

            uniqueLastKnotPositions.add(
                (knotPositions[lastKnotIndex][0], knotPositions[lastKnotIndex][1]))

    elif command == "L":
        for x in range(count):
            headPosition[0] -= 1
            tailPosition = updateTailPosition(headPosition, tailPosition)
            uniqueTailPositions.add((tailPosition[0], tailPosition[1]))

            knotPositions[0][0] = headPosition[0]

            for i in range(lastKnotIndex):
                knotPositions[i+1] = updateTailPosition(
                    knotPositions[i], knotPositions[i+1])

            uniqueLastKnotPositions.add(
                (knotPositions[lastKnotIndex][0], knotPositions[lastKnotIndex][1]))

    elif command == "U":
        for x in range(count):
            headPosition[1] += 1
            tailPosition = updateTailPosition(headPosition, tailPosition)
            uniqueTailPositions.add((tailPosition[0], tailPosition[1]))

            knotPositions[0][1] = headPosition[1]

            for i in range(lastKnotIndex):
                knotPositions[i+1] = updateTailPosition(
                    knotPositions[i], knotPositions[i+1])

            uniqueLastKnotPositions.add(
                (knotPositions[lastKnotIndex][0], knotPositions[lastKnotIndex][1]))

    elif command == "D":
        for x in range(count):
            headPosition[1] -= 1
            tailPosition = updateTailPosition(headPosition, tailPosition)
            uniqueTailPositions.add((tailPosition[0], tailPosition[1]))

            knotPositions[0][1] = headPosition[1]

            for i in range(lastKnotIndex):
                knotPositions[i+1] = updateTailPosition(
                    knotPositions[i], knotPositions[i+1])

            uniqueLastKnotPositions.add(
                (knotPositions[lastKnotIndex][0], knotPositions[lastKnotIndex][1]))

f.close()

# for p in uniqueLastKnotPositions:
#     print(p)

uniqueTailPositionsCount = len(uniqueTailPositions)
uniqueLastKnotPositionsCount = len(uniqueLastKnotPositions)

print(f"Part 1 answer: {uniqueTailPositionsCount}")
print(f"Part 2 answer: {uniqueLastKnotPositionsCount}")
