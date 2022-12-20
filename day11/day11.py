from math import prod


class Monkey:
    def __init__(self,
                 items: list[int],
                 operation: str,
                 divisibleTestNumber: int,
                 monkeyIndexIfTrue: int,
                 monkeyIndexIfFalse: int):
        self.items = items
        self.op = operation.split("=")[1].strip().replace("old", "item")
        self.divisibleTestNumber = divisibleTestNumber
        self.monkeyIndexIfTrue = monkeyIndexIfTrue
        self.monkeyIndexIfFalse = monkeyIndexIfFalse
        self.totalInspections = 0

    def operationNext(self):
        item = self.items.pop()
        ldic = locals()
        exec(f"item = {self.op}", {}, ldic)
        item = ldic["item"]
        return item

    def inspectNext(self, divideBy3: bool = True):
        item = self.operationNext()
        if divideBy3:
            item = item // 3
        else:
            global mod
            item = item % mod

        return (item, self.monkeyIndexIfTrue) if item % self.divisibleTestNumber == 0 else (item, self.monkeyIndexIfFalse)

    def incrementTotalInspections(self):
        self.totalInspections += 1


def nextLine(lines: list[str], lineIndex: int):
    lineIndex += 1
    return (lines[lineIndex].strip() if lineIndex < len(lines) else "", lineIndex)


def createMonkeys():
    f = open("input.txt", "r")

    lines = f.readlines()
    length = len(lines)
    lineIndex = -1
    line, lineIndex = nextLine(lines, lineIndex)
    monkeys: list[Monkey] = []

    while lineIndex < length:
        if line.startswith("Monkey"):
            line, lineIndex = nextLine(lines, lineIndex)

            items = []
            operation: str = ""
            divisibleTestNumber: int = 1
            monkeyIndexIfTrue: int = 0
            monkeyIndexIfFalse: int = 0

            while line != "":
                if line.startswith("Starting items:"):
                    split = line.replace(
                        "Starting items:", "").strip().split(", ")
                    for s in split:
                        items.append(int(s))
                elif line.startswith("Operation:"):
                    operation = line.replace("Operation:", "").strip()
                elif line.startswith("Test:"):
                    split = line.replace("Test:", "").strip().split(" ")
                    divisibleTestNumber = int(split[len(split) - 1])
                    for i in range(2):
                        line, lineIndex = nextLine(lines, lineIndex)
                        if line.startswith("If true:"):
                            split = line.replace(
                                "If true:", "").strip().split(" ")
                            monkeyIndexIfTrue = int(split[len(split) - 1])
                        elif line.startswith("If false:"):
                            split = line.replace(
                                "If false:", "").strip().split(" ")
                            monkeyIndexIfFalse = int(split[len(split) - 1])
                line, lineIndex = nextLine(lines, lineIndex)

            monkeys.append(Monkey(items, operation, divisibleTestNumber,
                                  monkeyIndexIfTrue, monkeyIndexIfFalse))

        line, lineIndex = nextLine(lines, lineIndex)

    f.close()

    return monkeys


monkeys: list[Monkey] = createMonkeys()

mod = prod([a.divisibleTestNumber for a in monkeys])

for i in range(20):
    for monkey in monkeys:
        for j in range(len(monkey.items)):
            monkey.incrementTotalInspections()
            item, nextMonkeyIndex = monkey.inspectNext()
            monkeys[nextMonkeyIndex].items.append(item)

totalInspectTimes = []
for monkey in monkeys:
    totalInspectTimes.append(monkey.totalInspections)

totalInspectTimes.sort(reverse=True)
totalMonkeyBusiness = totalInspectTimes[0] * totalInspectTimes[1]
print(f"Part 1 answer: {totalMonkeyBusiness}")

monkeys = createMonkeys()

for i in range(10000):
    monkeyIndex = 0
    for monkey in monkeys:
        for j in range(len(monkey.items)):
            monkey.incrementTotalInspections()
            item, nextMonkeyIndex = monkey.inspectNext(divideBy3=False)
            monkeys[nextMonkeyIndex].items.append(item)
        monkeyIndex += 1

totalInspectTimes = []
for monkey in monkeys:
    totalInspectTimes.append(monkey.totalInspections)

totalInspectTimes.sort(reverse=True)
totalMonkeyBusiness = totalInspectTimes[0] * totalInspectTimes[1]
print(f"Part 2 answer: {totalMonkeyBusiness}")
