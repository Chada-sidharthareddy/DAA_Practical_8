from collections import deque

def bfs(graph, start):

    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:

        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print("BFS Traversal:")
bfs(graph, 0)