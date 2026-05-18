"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node'], visited=None) -> Optional['Node']:
        if not visited:
            visited = {}
        if not node:
            return None
        
        if node.val in visited:
            return visited[node.val]
        
        neighborsCpy = []
        newNode = Node(node.val, neighborsCpy)
        visited[node.val] = newNode

        for neighbor in node.neighbors:
            neighborsCpy.append(self.cloneGraph(neighbor, visited))
        return newNode