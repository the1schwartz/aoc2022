f = open("input.txt", "r")

totalScore = 0
shapeScores = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

newTotalScore = 0
newShapeScores = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

for line in f:
    trimmedLine = line.strip()
    totalScore += shapeScores[trimmedLine]
    newTotalScore += newShapeScores[trimmedLine]

print(f"Part 1 answer: {totalScore}")
print(f"Part 2 answer: {newTotalScore}")
