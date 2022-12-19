def aStarAlgo(start_node, stop_node):
    open_set = set()
    open_set.add(start_node)
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}         # parents contains an adjacency map of all nodes
    # distance of starting node from itself is zero
    g[start_node] = 0
    # start_node is root node i.e it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        # node with lowest f() is found
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or graph_nodes[n] is None:
            pass
        else:
            for m in get_neighbors(n):
                # nodes 'm' not in first and last set are added to first
                # n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + 1
                # for each node m,compare its distance from start i.e g(m) to the
                # from start through n node
                else:
                    if g[m] > g[n] + 1:
                        # update g(m)
                        g[m] = g[n] + 1
                        # change parent of m to n
                        parents[m] = n
                        # if m in closed set,remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n is None:
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            return path
        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)
    return None


def get_neighbors(v):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return None


def heuristic(n):
    return h_dist[n]


f = open("input.txt", "r")

map = []

startPosition = (0, 0)
possibleStartPositions = []
endPosition = (0, 0)
currentPosition = [0, 0]
graph_nodes = {}
h_dist = {}

for line in f:
    trimmedLine = line.strip()
    list = []
    currentPosition[0] = 0
    for c in trimmedLine:

        if c == "S":
            startPosition = (currentPosition[0], currentPosition[1])
            possibleStartPositions.append(
                (currentPosition[0], currentPosition[1]))
            list.append(ord("a"))
        elif c == "a":
            possibleStartPositions.append(
                (currentPosition[0], currentPosition[1]))
            list.append(ord("a"))
        elif c == "E":
            endPosition = (currentPosition[0], currentPosition[1])
            list.append(ord("z"))
        else:
            list.append(ord(c))

        graph_nodes[f"{currentPosition[0]},{currentPosition[1]}"] = []
        currentPosition[0] += 1
    map.append(list)

    currentPosition[1] += 1

f.close()
width = len(map[0])
height = len(map)

for x in range(width):
    for y in range(height):
        nodeId = f"{x},{y}"
        nodeValue = map[y][x]
        x_dist = abs(endPosition[0] - x)
        y_dist = abs(endPosition[1] - y)
        h_dist[nodeId] = x_dist + y_dist

        rightX = x + 1
        leftX = x - 1
        upY = y - 1
        downY = y + 1

        if rightX < width:
            rightNodeId = f"{rightX},{y}"
            rightNodeValue = map[y][rightX]
            diff = rightNodeValue - nodeValue
            if diff <= 1:
                graph_nodes[nodeId].append(rightNodeId)

        if leftX >= 0:
            leftNodeId = f"{leftX},{y}"
            leftNodeValue = map[y][leftX]
            diff = leftNodeValue - nodeValue
            if diff <= 1:
                graph_nodes[nodeId].append(leftNodeId)

        if upY >= 0:
            upNodeId = f"{x},{upY}"
            upNodeValue = map[upY][x]
            diff = upNodeValue - nodeValue
            if diff <= 1:
                graph_nodes[nodeId].append(upNodeId)

        if downY < height:
            downNodeId = f"{x},{downY}"
            downNodeValue = map[downY][x]
            diff = downNodeValue - nodeValue
            if diff <= 1:
                graph_nodes[nodeId].append(downNodeId)

start = f"{startPosition[0]},{startPosition[1]}"
end = f"{endPosition[0]},{endPosition[1]}"

path = aStarAlgo(start, end)

print(f"Part 1 answer: {len(path) - 1}")

possiblePaths = []

for p in possibleStartPositions:
    start = f"{p[0]},{p[1]}"
    path = aStarAlgo(start, end)
    if path is not None:
        possiblePaths.append(len(path) - 1)

possiblePaths.sort()

print(f"Part 2 answer: {possiblePaths[0]}")
