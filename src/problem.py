"""
problem.py

This file defines an abstract 'Problem' class that serves as
the interface for all search problems.
"""

from abc import ABC, abstractmethod

class Problem(ABC):
    """
    This class is an abstract base class (ABC) for a search problem.
    It outlines the methods that any concrete problem implementation
    must provide.
    """

    @abstractmethod
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        pass

    @abstractmethod
    def isGoalState(self, state):
        """
        state: Search state
        Returns True if and only if 'state' is a goal state.
        """
        pass

    @abstractmethod
    def getSuccessors(self, state):
        """
        state: Search state
        
        For a given state, this should return a list of triples:
        (successor, action, stepCost)
        
        'successor' is a state reachable from 'state'
        'action' is the action required to get to 'successor'
        'stepCost' is the incremental cost of expanding to 'successor'
        """
        pass
