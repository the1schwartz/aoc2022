def moveCrates(moveMultipleInOneGo=False):
    f = open("input.txt", "r")

    crateLinesFinished = False
    stacks = []

    for line in f:
        trimmedLine = line.rstrip()

        if trimmedLine == "":
            crateLinesFinished = True

            for s in stacks:
                s.reverse()
            continue

        if not crateLinesFinished:
            if "[" not in trimmedLine:
                continue

            crates = [trimmedLine[i:i+4]
                      for i in range(0, len(trimmedLine), 4)]

            if len(stacks) == 0:
                for i in range(len(crates)):
                    stacks.append([])

            for i in range(len(crates)):
                c = crates[i]
                trimmed = c.strip()
                if trimmed == "":
                    continue
                c = trimmed.replace("[", "").replace("]", "")
                stacks[i].append(c)
        else:
            command = trimmedLine.replace("move ", "").replace(
                " from", "").replace(" to", "").strip().split(" ")
            command = [int(command[0]), int(
                command[1]) - 1, int(command[2]) - 1]

            if moveMultipleInOneGo:
                tmpStack = []
                for i in range(command[0]):
                    c = stacks[command[1]].pop()
                    tmpStack.append(c)
                for i in range(command[0]):
                    c = tmpStack.pop()
                    stacks[command[2]].append(c)
            else:

                for i in range(command[0]):
                    c = stacks[command[1]].pop()
                    stacks[command[2]].append(c)

    topOfStacks = ""
    for s in stacks:
        topOfStacks += s[len(s) - 1]

    return topOfStacks


print(f"Part 1 answer: {moveCrates()}")
print(f"Part 2 answer: {moveCrates(True)}")
