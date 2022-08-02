graph = [[]]


def path_finder(maze):
    lines = maze.split('\n')
    global graph
    graph = [[False] * len(lines) for i in range(len(lines))]
    for y in range(len(lines)):
        for x in range(len(lines)):
            if list(lines[y])[x] == 'W':
                graph[y][x] = True
            else:
                graph[y][x] = False
    go_to(0, 0)
    return graph[len(graph) - 1][len(graph) - 1]


def go_to(y, x):
    if y == -1 or y == len(graph) or x == -1 or x == len(graph) or graph[y][x]:
        return
    graph[y][x] = True
    go_to(y, x - 1)
    go_to(y, x + 1)
    go_to(y - 1, x)
    go_to(y + 1, x)


a = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...WW",
    "...W."])
print(path_finder(a))
