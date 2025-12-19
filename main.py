# main.py

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
# Let the user choose the maze
# ==============================
print("Choose a maze to run:")
print("1 - Easy (4x4)")
print("2 - Medium (10x20)")
print("3 - Hard (20x40)")

choice = input("Enter 1, 2, or 3: ").strip()

if choice == "1":
    maze = maze_easy
    START = start_easy
    GOAL = goal_easy
    maze_name = "Easy"
elif choice == "2":
    maze = maze_medium
    START = start_medium
    GOAL = goal_medium
    maze_name = "Medium"
elif choice == "3":
    maze = maze_hard
    START = start_hard
    GOAL = goal_hard
    maze_name = "Hard"
else:
    print("Invalid choice! Defaulting to Easy Maze.")
    maze = maze_easy
    START = start_easy
    GOAL = goal_easy
    maze_name = "Easy"

# ==============================
# Function to run an algorithm
# ==============================
def run_algorithm(name, func):
    print(f"\n--- {name} on {maze_name} Maze ---")
    start_time = time.time()
    path, nodes = func(maze, START, GOAL)
    end_time = time.time()
    time_ms = (end_time - start_time) * 1000

    if path:
        print(f"Path found: {path}")
        print(f"Path length: {len(path)}")
    else:
        print("No path found.")
    print(f"Nodes expanded: {nodes}")
    print(f"Time: {time_ms:.6f} ms")

# ==============================
# Run BFS, DFS, and A*
# ==============================
run_algorithm("BFS", bfs)
run_algorithm("DFS", dfs)
run_algorithm("A*", astar)
