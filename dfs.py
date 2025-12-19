# dfs.py
from maze import is_valid

def dfs(maze, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        (row, col), path = stack.pop()
        nodes_expanded += 1

        if (row, col) == goal:
            return path, nodes_expanded

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = row + dr, col + dc
            if is_valid(maze, nr, nc):
                stack.append(((nr, nc), path + [(nr, nc)]))

    return None, nodes_expanded
