"""
search.py

This file contains the generic search algorithms:
- Depth First Search (DFS)
- Breadth First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search (AStar)
"""

from src.utils import Stack, Queue, PriorityQueue
from src.problem import Problem

def depthFirstSearch(problem: Problem):
    """
    Search the deepest nodes in the search tree first.
    Returns a list of actions that reaches the goal.
    """
    fringe = Stack()
    fringe.push((problem.getStartState(), [])) # (state, path_to_state)
    visited = set()

    while not fringe.isEmpty():
        state, path = fringe.pop()

        if state in visited:
            continue
        visited.add(state)

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                new_path = path + [action]
                fringe.push((successor, new_path))
    
    return None # No solution found

def breadthFirstSearch(problem: Problem):
    """
    Search the shallowest nodes in the search tree first.
    Returns a list of actions that reaches the goal.
    """
    fringe = Queue()
    fringe.push((problem.getStartState(), [])) # (state, path_to_state)
    visited = set()

    while not fringe.isEmpty():
        state, path = fringe.pop()

        if state in visited:
            continue
        visited.add(state)

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                # To avoid adding the same state multiple times to the queue
                # we can check if it's already in the fringe.
                # For BFS, a simple 'visited' check on expansion is fine,
                # but adding it here makes it more efficient.
                # Let's add all successors and let the 'visited' check
                # at popping handle cycles.
                # A more optimized way:
                # if successor not in visited:
                #     visited.add(successor) # Mark as visited *on push*
                #     new_path = path + [action]
                #     fringe.push((successor, new_path))
                
                # The 'visited on pop' strategy is more general
                # and works for UCS/A* as well.
                new_path = path + [action]
                fringe.push((successor, new_path))
    
    return None # No solution found

def uniformCostSearch(problem: Problem):
    """
    Search the node of least total cost first.
    Returns a list of actions that reaches the goal.
    """
    fringe = PriorityQueue()
    fringe.push((problem.getStartState(), [], 0), 0) # (state, path, cost), priority
    visited = set()

    while not fringe.isEmpty():
        state, path, cost = fringe.pop()

        if state in visited:
            continue
        visited.add(state)

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                new_path = path + [action]
                new_cost = cost + stepCost
                fringe.push((successor, new_path, new_cost), new_cost)
    
    return None # No solution found

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state
    to the nearest goal in the provided SearchProblem.
    This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: Problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    Returns a list of actions that reaches the goal.
    """
    fringe = PriorityQueue()
    start_state = problem.getStartState()
    h = heuristic(start_state, problem)
    fringe.push((start_state, [], 0), 0 + h) # (state, path, g_cost), f_cost
    visited = set()

    while not fringe.isEmpty():
        state, path, g_cost = fringe.pop()

        if state in visited:
            continue
        visited.add(state)

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                new_path = path + [action]
                new_g_cost = g_cost + stepCost
                h_cost = heuristic(successor, problem)
                f_cost = new_g_cost + h_cost
                fringe.push((successor, new_path, new_g_cost), f_cost)
    
    return None # No solution found
