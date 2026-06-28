"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        queue = deque([root])
        while queue:
            prev = None
            for _ in range(len(queue)):
                cur = queue.popleft()
                if not prev:
                    prev = cur
                else:
                    prev.next = cur
                    prev = cur
                
                if cur.left:   # since bst is perfect, left child implies right must also exist
                    queue.append(cur.left)
                    queue.append(cur.right)


        return root