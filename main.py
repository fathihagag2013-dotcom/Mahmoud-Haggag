# main.py
import time
from maze import maze, START, GOAL
from bfs import bfs
from dfs import dfs
from astar import astar

def run_algorithm(name, func):
    print(f"\n{name}")
    start_time = time.time()
    path, nodes = func(maze, START, GOAL)
    end_time = time.time()

    print("Path:", path)
    print("Path length:", len(path) if path else "No path")
    print("Nodes expanded:", nodes)
    print("Time:", round(end_time - start_time, 6), "seconds")

run_algorithm("BFS", bfs)
run_algorithm("DFS", dfs)
run_algorithm("A*", astar)
