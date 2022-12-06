charPriorities = {}
f = open("input.txt", "r")

value = 1
for i in range(ord('a'), ord('z')+1):
    charPriorities[chr(i)] = value
    value += 1

for i in range(ord('A'), ord('Z')+1):
    charPriorities[chr(i)] = value
    value += 1

prioritySum = 0

group = []
badgePrioritySum = 0
for line in f:
    trimmedLine = line.strip()
    group.append(trimmedLine)

    if len(group) == 3:
        commonChars = list(set(group[0]) & set(group[1]) & set(group[2]))
        badgePrioritySum += charPriorities[commonChars[0]]
        group.clear()

    size = int(len(trimmedLine) / 2)
    compartments = [trimmedLine[i:i+size]
                    for i in range(0, len(trimmedLine), size)]
    commonChars = list(set(compartments[0]) & set(compartments[1]))
    prioritySum += charPriorities[commonChars[0]]

f.close()

print(f"Part 1 answer: {prioritySum}")
print(f"Part 2 answer: {badgePrioritySum}")
