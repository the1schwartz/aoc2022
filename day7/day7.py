class TreeNode:
    def __init__(self, name: str):
        self.name: str = name
        self.isDir: bool = True
        self.children = []
        self.childrenMap = {}
        self.size: int = 0
        self.parent: TreeNode = None


def postorder_traversal_iteratively(root: TreeNode):
    result = []
    if not root:
        return result
    stack = [root]
    # used to record whether one child has been visited
    last = None

    while stack:
        root = stack[-1]
        # if current node has no children, or one child has been visited, then process and pop it
        if not root.children or last and (last in root.children):

            if root.parent:
                root.parent.size += root.size
            result.append(root)

            stack.pop()
            last = root
        # if not, push children in stack
        else:
            # push in reverse because of FILO, if you care about that
            for child in root.children[::-1]:
                stack.append(child)

    return result


rootNode: TreeNode = None
currentNode: TreeNode = None
f = open("input.txt", "r")

for line in f:
    trimmedLine = line.strip()

    if trimmedLine.startswith("$"):
        split = trimmedLine.split(" ")
        command = split[1]

        if command == "cd":
            dirName = split[2]

            if dirName == "/":
                rootNode = TreeNode("/")
                currentNode = rootNode
            elif dirName == "..":
                currentNode = currentNode.parent
            else:
                currentNode = currentNode.childrenMap[dirName]
        elif command == "ls":
            pass
    else:
        split = trimmedLine.split(" ")
        name = split[1]
        node = TreeNode(name)

        if split[0] != "dir":
            node.size = int(split[0])
            node.isDir = False

        node.parent = currentNode
        currentNode.childrenMap[name] = node
        currentNode.children.append(node)

f.close()

nodes = postorder_traversal_iteratively(rootNode)

totalUsedSize = rootNode.size
totalDiskSize = 70000000
requiredUnusedSpace = 30000000
unusedSize = totalDiskSize - totalUsedSize
minRequiredSize = requiredUnusedSpace - unusedSize
minSize = requiredUnusedSpace

sum = 0
for node in nodes:
    if node.isDir and node.size <= 100000:
        sum += node.size
    if node.isDir and node.size >= minRequiredSize:
        minSize = min(node.size, minSize)

print(f"Part 1 answer: {sum}")
print(f"Part 2 answer: {minSize}")
