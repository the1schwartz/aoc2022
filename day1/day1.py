f = open("input.txt", "r")

currentCalories = 0
elvesCalories = []

for line in f:
    trimmedLine = line.strip()
    if trimmedLine == "":
        elvesCalories.append(currentCalories)
        currentCalories = 0
        continue

    currentCalories += int(trimmedLine)

f.close()

if currentCalories > 0:
    elvesCalories.append(currentCalories)

top3ElvesCalories = sorted(elvesCalories, reverse=True)[:3]

totalTop3Calories = 0
for x in top3ElvesCalories:
    totalTop3Calories += x

print(f"Part 1 answer: {top3ElvesCalories[0]}")
print(f"Part 2 answer: {totalTop3Calories}")
