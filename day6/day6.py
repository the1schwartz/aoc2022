def findMarker(data: str, n: int):
    index = -1
    for i in range(len(data)):
        s = set(list(data[i:i+n]))
        size = len(s)
        if size == n:
            index = i + n
            break
    return index


f = open("input.txt", "r")
data = f.read()
f.close()

index = findMarker(data, 4)

print(f"Part 1 answer: {index}")

index = findMarker(data, 14)

print(f"Part 2 answer: {index}")
