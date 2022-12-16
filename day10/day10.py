def runCycle():
    global cycleCount
    global currentPixelIndex
    global registerX
    global pixels

    cycleCount += 1
    updateSignalStrength()

    currentPixelX = currentPixelIndex[0]
    currentPixelY = currentPixelIndex[1]

    if currentPixelX >= (registerX - 1) and currentPixelX <= (registerX + 1):
        pixels[currentPixelY][currentPixelX] = "#"

    currentPixelX += 1
    currentPixelX = currentPixelX % 40

    if currentPixelX == 0:
        currentPixelY += 1

    currentPixelIndex[0] = currentPixelX
    currentPixelIndex[1] = currentPixelY


def updateSignalStrength():
    global signalStrengths
    currentSignalStrength = cycleCount * registerX
    if cycleCount in cycleChecks:
        signalStrengths.append(currentSignalStrength)


cycleCount = 0
registerX = 1
cycleChecks = [20, 60, 100, 140, 180, 220]
signalStrengths = []

pixels = []
currentPixelIndex = [0, 0]

for y in range(6):
    pixels.append([])
    for x in range(40):
        pixels[y].append(".")


f = open("input.txt", "r")

for line in f:
    trimmedLine = line.strip()
    split = trimmedLine.split(" ")
    command = split[0]

    if command == "noop":
        runCycle()
    elif command == "addx":
        value = int(split[1])
        runCycle()
        runCycle()
        registerX += value

f.close()

signalStrengthsSum = 0

for ss in signalStrengths:
    signalStrengthsSum += ss

print(f"Part 1 answer: {signalStrengthsSum}")

print("Part 2 answer:")
for y in range(6):
    s = ""
    for x in range(40):
        s += str(pixels[y][x])
    print(s)
