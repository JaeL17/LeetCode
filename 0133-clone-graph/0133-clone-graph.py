"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Dictionary to save original node -> cloned node mapping
        visited = {}

        # Initialize the stack with the starting node
        stack = [node]
        visited[node] = Node(node.val)

        while stack:
            curr = stack.pop()

            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and add it to the visited map
                    visited[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                # Link the clone of the neighbor to the clone of the current node
                visited[curr].neighbors.append(visited[neighbor])

        return visited[node]