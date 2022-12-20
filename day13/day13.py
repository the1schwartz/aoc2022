from copy import deepcopy


def bubbleSort(list):
    n = len(list)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if not isRightOrder(deepcopy(list[j]), deepcopy(list[j + 1])):
                swapped = True
                list[j], list[j + 1] = list[j + 1], list[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


f = open("input.txt", "r")

pairs = []
currentPair = []
packetLists = []

for line in f:
    trimmedLine = line.strip()

    if trimmedLine == "":
        pairs.append(currentPair)
        currentPair = []
    else:
        command = f"packets = {trimmedLine}"
        ldic = locals()
        exec(command, {}, ldic)
        currentPair.append(ldic["packets"])
        packetLists.append(deepcopy(ldic["packets"]))

if currentPair:
    pairs.append(currentPair)

f.close()

pairsInRightOrder = []
currentPair = 1


def isRightOrder(leftList, rightList):
    leftStack = []
    rightStack = []

    result = True

    leftStack.append(leftList)
    rightStack.append(rightList)
    rootLogDisplayed = False

    while leftStack:
        left = leftStack.pop()

        if not rightStack:
            result = False
            break

        right = rightStack.pop()

        isLeftList = type(left) == list
        isRightList = type(right) == list

        if isLeftList and not isRightList:
            leftStack.append(left)
            rightStack.append([right])
        elif not isLeftList and isRightList:
            rightStack.append(right)
            leftStack.append([left])
        elif not isLeftList and not isRightList:
            if left == right:
                continue
            elif left < right:
                break
            elif left > right:
                result = False
                break
        elif isLeftList and isRightList:
            if left and right:
                first = left.pop(0)
                leftStack.append(left)
                leftStack.append(first)

                first = right.pop(0)
                rightStack.append(right)
                rightStack.append(first)
            elif not left and not right:
                continue
            elif not left:
                break
            elif not right:
                result = False
                break

    return result


for pair in pairs:
    leftList = pair[0]
    rightList = pair[1]

    pairInRightOrder = isRightOrder(leftList, rightList)

    if pairInRightOrder:
        pairsInRightOrder.append(currentPair)

    currentPair += 1

sumPairsInRightOrder = 0

for index in pairsInRightOrder:
    sumPairsInRightOrder += index

print(f"Part 1 answer: {sumPairsInRightOrder}")

packetLists.append([[2]])
packetLists.append([[6]])

bubbleSort(packetLists)

dividerPackets = ["[[2]]", "[[6]]"]
dividerPacketIndices = []

i = 1
for packetList in packetLists:
    s = str(packetList)

    if s in dividerPackets:
        dividerPacketIndices.append(i)

        if len(dividerPacketIndices) == 2:
            break

    i += 1

dividerPacketsProduct = dividerPacketIndices[0] * dividerPacketIndices[1]

print(f"Part 2 answer: {dividerPacketsProduct}")
