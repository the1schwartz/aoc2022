f = open("input.txt", "r")

fullyContainedCount = 0
overlapCount = 0
for line in f:
    trimmedLine = line.strip()
    pairs = trimmedLine.split(",")
    firstPair = pairs[0].split("-")
    secondPair = pairs[1].split("-")
    firstLow = int(firstPair[0])
    firstHigh = int(firstPair[1])
    secondLow = int(secondPair[0])
    secondHigh = int(secondPair[1])

    if firstLow <= secondLow and firstHigh >= secondLow or \
            firstLow <= secondHigh and firstHigh >= secondHigh or \
            secondLow <= firstLow and secondHigh >= firstLow or \
            secondLow <= firstHigh and secondHigh >= firstHigh:

        overlapCount += 1

        if firstLow <= secondLow and firstHigh >= secondHigh or \
                firstLow >= secondLow and firstHigh <= secondHigh:
            fullyContainedCount += 1

print(f"Part 1 answer: {fullyContainedCount}")
print(f"Part 2 answer: {overlapCount}")
