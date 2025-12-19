# bfs.py
from collections import deque
from maze import is_valid

def bfs(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])
    nodes_expanded = 0

    while queue:
        (row, col), path = queue.popleft()
        nodes_expanded += 1

        if (row, col) == goal:
            return path, nodes_expanded

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = row + dr, col + dc
            if is_valid(maze, nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None, nodes_expanded
