# maze.py

maze = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

START = (0, 0)
GOAL = (4, 4)

ROWS = len(maze)
COLS = len(maze[0])


def is_valid(maze, row, col):
    return (
        0 <= row < ROWS and
        0 <= col < COLS and
        maze[row][col] == 0
    )
