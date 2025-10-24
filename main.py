"""
main.py

This is the main executable script for the AI Search Toolkit.
It uses argparse to parse command-line arguments and runs the
specified search algorithm on the given maze file.

Example Usage:
python main.py data/maze_medium.txt -a a_star
"""

import argparse
import time
from src.maze_problem import MazeProblem, manhattanHeuristic
import src.search as search

def main():
    """
    Parses command-line arguments and executes the search.
    """
    parser = argparse.ArgumentParser(
        description="Solve a maze file using AI search algorithms."
    )
    
    parser.add_argument(
        'maze_file', 
        type=str, 
        help="Path to the .txt maze file (e.g., data/maze_medium.txt)"
    )
    
    parser.add_argument(
        '-a', '--algorithm', 
        type=str, 
        default='dfs', 
        choices=['dfs', 'bfs', 'ucs', 'a_star'],
        help="The search algorithm to use (default: dfs)"
    )
    
    args = parser.parse_args()
    
    print(f"Loading maze from: {args.maze_file}")
    problem = MazeProblem(args.maze_file)
    
    print(f"Solving using {args.algorithm.upper()}...")
    
    # Select algorithm
    alg_map = {
        'dfs': search.depthFirstSearch,
        'bfs': search.breadthFirstSearch,
        'ucs': search.uniformCostSearch,
        'a_star': lambda p: search.aStarSearch(p, heuristic=manhattanHeuristic)
    }
    
    algorithm = alg_map.get(args.algorithm)
    
    if algorithm is None:
        print(f"Error: Unknown algorithm '{args.algorithm}'")
        return
        
    start_time = time.time()
    solution = algorithm(problem)
    end_time = time.time()
    
    # Print results
    print("-" * 30)
    if solution is not None:
        print("🎉 Solution Found! 🎉")
        print(f"Path: {' -> '.join(solution)}")
        print(f"Path Length: {len(solution)} steps")
    else:
        print("💔 No solution found.")
    
    print(f"Time elapsed: {end_time - start_time:.6f} seconds")
    print("-" * 30)


if __name__ == "__main__":
    main()
