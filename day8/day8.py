trees = []

f = open("input.txt", "r")

width = 0
height = 0

for line in f:
    trimmedLine = line.strip()
    width = len(trimmedLine)
    row = []
    for c in trimmedLine:
        row.append(int(c))
    trees.append(row)
    height += 1

f.close()

totalVisibleTrees = 0
highestTreeScore = 0

for x in range(width):
    for y in range(height):
        if x == 0 or y == 0 or x == (width - 1) or y == (height - 1):
            totalVisibleTrees += 1
            continue

        currentTreeHeight: int = trees[y][x]
        treesLeftOfCurrentTree = trees[y][:x]

        # left of current tree
        isTreeVisible = True
        for i in range(x):
            t: int = trees[y][i]
            if currentTreeHeight <= t:
                isTreeVisible = False
                break

        if not isTreeVisible:
            # right of current tree
            isTreeVisible = True
            for i in range(x + 1, width):
                t: int = trees[y][i]
                if currentTreeHeight <= t:
                    isTreeVisible = False
                    break

            if not isTreeVisible:
                # above of current tree
                isTreeVisible = True
                for j in range(y):
                    t: int = trees[j][x]
                    if currentTreeHeight <= t:
                        isTreeVisible = False
                        break

                if not isTreeVisible:
                    # below of current tree
                    isTreeVisible = True
                    for j in range(y + 1, height):
                        t: int = trees[j][x]
                        if currentTreeHeight <= t:
                            isTreeVisible = False
                            break

        if isTreeVisible:
            totalVisibleTrees += 1

        leftScore = 0
        rightScore = 0
        aboveScore = 0
        belowScore = 0
        # left of current tree
        for i in range(x - 1, -1, -1):
            t: int = trees[y][i]
            leftScore += 1
            if currentTreeHeight <= t:
                break

        # right of current tree
        for i in range(x + 1, width):
            t: int = trees[y][i]
            rightScore += 1
            if currentTreeHeight <= t:
                break

        # above of current tree
        for j in range(y - 1, -1, -1):
            t: int = trees[j][x]
            aboveScore += 1
            if currentTreeHeight <= t:
                break

        # below of current tree
        for j in range(y + 1, height):
            t: int = trees[j][x]
            belowScore += 1
            if currentTreeHeight <= t:
                break

        highestTreeScore = max(
            highestTreeScore, (leftScore
                               * rightScore * aboveScore * belowScore))


print(f"Part 1 answer: {totalVisibleTrees}")
print(f"Part 2 answer: {highestTreeScore}")
