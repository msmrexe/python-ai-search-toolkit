"""
utils.py

This file contains the data structures (Stack, Queue, PriorityQueue)
used by the generic search algorithms.
"""

import collections
import heapq

class Stack:
    "A container with a LIFO (Last-In, First-Out) queuing policy."
    def __init__(self):
        self.list = []

    def push(self, item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

class Queue:
    "A container with a FIFO (First-In, First-Out) queuing policy."
    def __init__(self):
        self.queue = collections.deque()

    def push(self, item):
        "Enqueue 'item' into the queue"
        self.queue.append(item)

    def pop(self):
        "Dequeue the earliest enqueued item from the queue"
        return self.queue.popleft()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.queue) == 0

class PriorityQueue:
    "A container where items are retrieved based on priority."
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        "Push 'item' onto the priority queue with 'priority'."
        # We use 'self.count' as a tie-breaker to ensure FIFO
        # for items with the same priority
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        "Pop the item with the lowest priority."
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        "Returns true if the priority queue is empty."
        return len(self.heap) == 0

    def update(self, item, priority):
        "Update the priority of an existing 'item' in the queue."
        # This implementation is a bit more complex. For this project,
        # we'll assume we only push and never update, as A*
        # with a consistent heuristic doesn't need to re-open nodes
        # if we also keep track of visited states.
        # A more robust implementation would search for 'item'
        # and update its priority.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p > priority:
                    self.heap[index] = (priority, c, item)
                    heapq.heapify(self.heap)
                return
        # If item not found, just push it
        self.push(item, priority)
