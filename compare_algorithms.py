# compare_algorithms.py

import time
from bfs import bfs
from dfs import dfs
from astar import astar
from maze import (
    maze_easy, start_easy, goal_easy,
    maze_medium, start_medium, goal_medium,
    maze_hard, start_hard, goal_hard
)

# ==============================
# Maze scenarios
# ==============================
mazes = [
    ("Easy", maze_easy, start_easy, goal_easy),
    ("Medium", maze_medium, start_medium, goal_medium),
    ("Hard", maze_hard, start_hard, goal_hard)
]

algorithms = [
    ("BFS", bfs),
    ("DFS", dfs),
    ("A*", astar)
]

# ==============================
# Run all algorithms on all mazes
# ==============================
print(f"{'Maze':<10} | {'Algorithm':<5} | {'Path Length':<12} | {'Nodes Expanded':<15} | {'Time (ms)':<10}")
print("-" * 75)

for maze_name, maze, START, GOAL in mazes:
    for alg_name, alg in algorithms:
        start_time = time.time()
        path, nodes = alg(maze, START, GOAL)
        end_time = time.time()

        path_len = len(path) if path else "No Path"
        time_ms = (end_time - start_time) * 1000

        print(f"{maze_name:<10} | {alg_name:<9} | {str(path_len):<12} | {nodes:<15} | {time_ms:.6f}")

# ==============================


