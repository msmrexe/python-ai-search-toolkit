# AI Search Algorithm Toolkit (Python)

This project provides a clean, modular Python implementation of foundational AI search algorithms (DFS, BFS, UCS, and A\*) for an Artificial Intelligence course. It is designed to be a flexible toolkit capable of solving problems defined by an abstract `Problem` class, with a concrete example provided for solving grid-based mazes.

## Features

  * **Modular Design:** Algorithms are decoupled from the problem definition.
  * **Generic Algorithms:** Clean implementations of:
      * Depth First Search (DFS)
      * Breadth First Search (BFS)
      * Uniform Cost Search (UCS)
      * A\* Search (AStar)
  * **Concrete Example:** A `MazeProblem` class that parses `.txt` files.
  * **Heuristics:** Includes a sample `manhattanHeuristic` for A\*.
  * **Command-Line Interface:** A `main.py` script using `argparse` to easily run any algorithm on any maze.

## AI & CS Concepts Showcased

  * **Problem Abstraction:** Use of Abstract Base Classes (`abc.ABC`) to define a formal `Problem` interface (`getStartState`, `isGoalState`, `getSuccessors`).
  * **Search Algorithms:** Implementation of uninformed (DFS, BFS) and informed (UCS, A\*) graph search algorithms.
  * **Data Structures:** Practical application of Stacks, Queues, and Priority Queues (`heapq`) as the "fringe" for different search strategies.
  * **Heuristics:** Understanding the role of a heuristic function ($h(n)$) in A\* and implementing the admissible and consistent Manhattan distance heuristic.
  * **State-Space Search:** The entire project is a classic example of state-space search, including managing a `visited` set to avoid cycles.
  * **Software Design:** Clean, modular code separated into `problem`, `search`, and `utils` components.

---

## How It Works

The system is built on a few core components:

### 1\. The `Problem` Interface (`src/problem.py`)

This abstract class defines the "contract" for a search problem. Any problem (like a maze, 8-puzzle, etc.) must provide three methods: `getStartState()`, `isGoalState(state)`, and `getSuccessors(state)`.

### 2\. Utility Data Structures (`src/utils.py`)

This file contains the `Stack` (for DFS), `Queue` (for BFS), and `PriorityQueue` (for UCS/A\*) classes that the search algorithms use to manage the "fringe" (the set of nodes to be explored).

### 3\. The `MazeProblem` (`src/maze_problem.py`)

This is a concrete implementation of the `Problem` interface.

  * Its `__init__` method reads a `.txt` file, parsing it into a grid, and identifying walls (`%`), the start (`S`), and the goal (`G`).
  * `getSuccessors(state)` returns valid moves (North, South, East, West) from the current `(row, col)` state that are not walls.
  * This file also contains the `manhattanHeuristic` function, which is passed to A\* to guide its search.

### 4\. The Search Algorithms (`src/search.py`)

This file contains the core logic for each search algorithm. They are all generic and operate on any object that adheres to the `Problem` interface.

The algorithms are split into two categories: **Uninformed** (they only know the problem definition) and **Informed** (they use extra knowledge, like cost or heuristics).

#### Uninformed Search Strategies

  * **Depth First Search (DFS):**

      * **Strategy:** Explores as deeply as possible along one branch before backtracking. It expands the "deepest" node in the fringe.
      * **Data Structure:** Implemented using a **Stack** (Last-In, First-Out).
      * **Optimality:** Not optimal. It will find *a* solution, but not guaranteed to be the shortest one.

  * **Breadth First Search (BFS):**

      * **Strategy:** Explores all neighbor nodes at the present depth layer by layer before moving on to the next depth level. It expands the "shallowest" node.
      * **Data Structure:** Implemented using a **Queue** (First-In, First-Out).
      * **Optimality:** Optimal *if* all step costs are equal (like in our basic maze). It is guaranteed to find the path with the fewest steps.

#### Informed Search Strategies

  * **Uniform Cost Search (UCS):**

      * **Strategy:** Explores nodes based on the lowest cumulative cost from the start. It expands the node with the lowest path cost $g(n)$.
      * **Data Structure:** Implemented using a **Priority Queue**.
      * **Priority:** $g(n)$, where $g(n)$ is the cost of the path from the start node to node $n$.
      * **Optimality:** Optimal and complete. It is guaranteed to find the path with the lowest total cost, regardless of the number of steps.

  * **A\* Search (AStar):**

      * **Strategy:** The smartest algorithm in this toolkit. It combines the cost-to-reach $g(n)$ with an *estimated* cost-to-goal $h(n)$. It expands the node with the lowest $f(n)$ value.
      * **Data Structure:** Implemented using a **Priority Queue**.
      * **Priority:** $f(n) = g(n) + h(n)$
          * $g(n)$: The known cost from the start to the current node $n$ (same as UCS).
          * $h(n)$: The **heuristic function**—an *estimated* cost from node $n$ to the goal.
      * **Optimality:** A\* is optimal and complete *if* its heuristic $h(n)$ is **admissible** (it never overestimates the true cost) and **consistent**. The `manhattanHeuristic` used in this project is both admissible and consistent.

### 5\. The Main Executable (`main.py`)

This script ties everything together.

1.  It uses `argparse` to read user input from the command line (the maze file path and the algorithm to use).
2.  It instantiates a `MazeProblem` object using the file.
3.  It calls the correct search function from `src/search.py`.
4.  It prints the solution, path length, and execution time.

---

## Project Structure

```
python-ai-search-toolkit/
├── .gitignore
├── LICENSE
├── README.md
├── main.py                         # Main runnable script
├── data/                           # Sample mazes
│   ├── maze_medium.txt
│   ├── maze_no_solution.txt
│   └── maze_small.txt
└── src/
    ├── __init__.py                 # Makes 'src' a package
    ├── maze_problem.py             # Concrete implementation for mazes
    ├── problem.py                  # Abstract Problem class
    ├── search.py                   # Generic search algorithms (DFS, BFS, etc.)
    └── utils.py                    # Stack, Queue, PriorityQueue
```

## How to Use

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/msmrexe/python-ai-search-toolkit.git
    cd python-ai-search-toolkit
    ```

2.  **Run an Algorithm:**
    The `main.py` script is used to run the searches. The basic syntax is:
    `python main.py <path_to_maze_file> --algorithm <algorithm_name>`

    **Example (A\*):**

    ```bash
    python main.py data/maze_medium.txt -a a_star
    ```

    *Output:*

    ```
    Loading maze from: data/maze_medium.txt
    Solving using A_STAR...
    ------------------------------
    🎉 Solution Found! 🎉
    Path: South -> South -> ... -> East -> East
    Path Length: 58 steps
    Time elapsed: 0.001967 seconds
    ------------------------------
    ```

    **Example (BFS):**

    ```bash
    python main.py data/maze_medium.txt -a bfs
    ```

    *Output:*

    ```
    Loading maze from: data/maze_medium.txt
    Solving using BFS...
    ------------------------------
    🎉 Solution Found! 🎉
    Path: South -> South -> ... -> East -> East
    Path Length: 58 steps
    Time elapsed: 0.002980 seconds
    ------------------------------
    ```

    **Example (No Solution):**

    ```bash
    python main.py data/maze_no_solution.txt -a dfs
    ```

    *Output:*

    ```
    Loading maze from: data/maze_no_solution.txt
    Solving using DFS...
    ------------------------------
    💔 No solution found.
    Time elapsed: 0.000100 seconds
    ------------------------------
    ```

---

## Author

Feel free to connect or reach out if you have any questions!

* **Maryam Rezaee**
* **GitHub:** [@msmrexe](https://github.com/msmrexe)
* **Email:** [ms.maryamrezaee@gmail.com](mailto:ms.maryamrezaee@gmail.com)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.
