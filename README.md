# Maze Solving Using Search Algorithms (BFS, DFS, A*)

## Team members roles
محمود محمد فتحي عثمان حجاج : BFS , DFS

محمد البسيوني محمد احمد موسي اسماعيل : *A

---

## 📌 Overview
This project solves the **Maze Solving problem** using classical search algorithms in Artificial Intelligence. The objective is to navigate an agent from a start position to a goal position in a grid-based maze while avoiding obstacles.

The project demonstrates and compares the behavior and performance of:
- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **A* Search (A-Star)**

The comparison focuses on **optimality, completeness, time complexity, space complexity, and practical performance**.

---

## 🧩 Problem Description
A maze is represented as a two-dimensional grid where:
- `0` represents a free cell
- `1` represents a wall (blocked cell)

The agent:
- Starts at a predefined **start cell**
- Can move **up, down, left, or right**
- Must reach the **goal cell** using valid moves

Each move has a uniform cost of **1**.

---

## 🧠 State-Space Formulation

- **State:** `(row, column)`
- **Initial State:** Start position
- **Actions:** Move Up, Down, Left, Right
- **Transition Model:** Move to an adjacent free cell
- **Goal Test:** Current state equals the goal position
- **Path Cost:** Number of steps taken

---

## ⚙️ Algorithms Implemented

### 🔍 Breadth-First Search (BFS)
BFS explores the maze level by level, expanding all nodes at the current depth before moving deeper.

**Properties:**
- Complete: ✅ Yes
- Optimal: ✅ Yes (uniform step cost)
- Time Complexity: `O(V + E)`
- Space Complexity: `O(V)`

---

### 🌲 Depth-First Search (DFS)
DFS explores as deep as possible along a path before backtracking.

**Properties:**
- Complete: ❌ No (in infinite or cyclic spaces)
- Optimal: ❌ No
- Time Complexity: `O(V + E)`
- Space Complexity: `O(V)`

---

### ⭐ A* Search Algorithm
A* is an informed search algorithm that uses a heuristic to guide the search toward the goal.

**Evaluation Function:**
```
f(n) = g(n) + h(n)
```
where:
- `g(n)` = cost from the start to node `n`
- `h(n)` = heuristic estimate to the goal

**Heuristic Used:** Manhattan Distance
```
h(n) = |x1 - x2| + |y1 - y2|
```

**Properties:**
- Complete: ✅ Yes
- Optimal: ✅ Yes (admissible heuristic)
- Time Complexity: Exponential (worst case)
- Space Complexity: `O(V)`

---

## 📊 Performance Comparison

| Algorithm | Complete | Optimal | Time Complexity | Space Complexity | Notes |
|---------|----------|---------|-----------------|------------------|------|
| BFS     | Yes      | Yes     | O(V + E)        | O(V)             | Guarantees shortest path |
| DFS     | No       | No      | O(V + E)        | O(V)             | Memory-efficient but unreliable |
| A*      | Yes      | Yes     | Exponential     | O(V)             | Best practical performance |

---

## 🧪 Experimental Results
During execution, each algorithm reports:
- Path found
- Path length
- Number of nodes expanded
- Execution time

These metrics highlight the efficiency advantages of heuristic-guided search (A*) over uninformed methods (BFS and DFS).

---




## 📁 Project Structure
```
Maze project/
│
├── run_algorithms.py
├── main.py
├── maze.py
├── bfs.py
├── dfs.py
└── astar.py
```

---

## 📝 Conclusion
- **BFS** guarantees the shortest path but requires significant memory.
- **DFS** is memory-efficient but does not guarantee optimal solutions.
- **A*** provides the best balance between efficiency and optimality using heuristic guidance.

A* is the preferred algorithm for maze-solving problems when an admissible heuristic is available.



