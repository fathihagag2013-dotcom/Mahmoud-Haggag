# astar.py
import heapq
from maze import is_valid

def heuristic(a, b):
    # Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    pq = []
    heapq.heappush(pq, (0, 0, start, [start]))
    visited = set()
    nodes_expanded = 0

    while pq:
        f, g, (row, col), path = heapq.heappop(pq)
        nodes_expanded += 1

        if (row, col) == goal:
            return path, nodes_expanded

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = row + dr, col + dc
            if is_valid(maze, nr, nc):
                new_g = g + 1
                new_f = new_g + heuristic((nr, nc), goal)
                heapq.heappush(
                    pq,
                    (new_f, new_g, (nr, nc), path + [(nr, nc)])
                )

    return None, nodes_expanded
