"""
maze_problem.py

This file defines the concrete MazeProblem class, which
implements the abstract Problem interface for a grid-based maze.
"""

from src.problem import Problem

class MazeProblem(Problem):
    """
    A class to represent a search problem in a grid-based maze.
    The maze is read from a text file.
    'S' = Start
    'G' = Goal
    '%' = Wall
    ' ' = Open path
    """

    def __init__(self, maze_file_path):
        """
        Parses the maze file and initializes the problem state.
        """
        self.grid = []
        self.walls = set()
        self.startState = None
        self.goalState = None
        
        try:
            with open(maze_file_path, 'r') as f:
                for r, line in enumerate(f):
                    row = []
                    for c, char in enumerate(line.strip()):
                        row.append(char)
                        if char == '%':
                            self.walls.add((r, c))
                        elif char == 'S':
                            self.startState = (r, c)
                        elif char == 'G':
                            self.goalState = (r, c)
                    self.grid.append(row)
        
            if self.startState is None or self.goalState is None:
                raise ValueError("Maze file must contain one 'S' and one 'G'.")
            
            self.height = len(self.grid)
            self.width = len(self.grid[0]) if self.height > 0 else 0

        except FileNotFoundError:
            print(f"Error: The file '{maze_file_path}' was not found.")
            exit(1)
        except Exception as e:
            print(f"Error parsing maze file: {e}")
            exit(1)

    def getStartState(self):
        """Returns the start state (r, c) tuple."""
        return self.startState

    def isGoalState(self, state):
        """Returns True if the state is the goal state."""
        return state == self.goalState

    def getSuccessors(self, state):
        """
        Returns a list of (successor, action, stepCost) triples
        for the given state.
        """
        successors = []
        r, c = state

        # Define possible actions: (action_name, (dr, dc))
        possible_actions = [
            ('North', (-1, 0)),
            ('South', (1, 0)),
            ('West',  (0, -1)),
            ('East',  (0, 1)),
        ]

        for action, (dr, dc) in possible_actions:
            next_r, next_c = r + dr, c + dc
            next_state = (next_r, next_c)

            # Check if the next state is within bounds and not a wall
            if (0 <= next_r < self.height and
                0 <= next_c < self.width and
                next_state not in self.walls):
                
                successors.append((next_state, action, 1))
        
        return successors

def manhattanHeuristic(state, problem: MazeProblem):
    """
    A heuristic for the MazeProblem.
    Calculates the Manhattan distance from the state to the goal.
    """
    (r1, c1) = state
    (r2, c2) = problem.goalState
    return abs(r1 - r2) + abs(c1 - c2)
