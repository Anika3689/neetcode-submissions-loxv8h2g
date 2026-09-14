"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
            
        nodeCopies = {} # keys are (node.val, node.next)
        cur = head
        while cur:
            nodeCopies[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            curCpy = nodeCopies[cur]
            curCpy.next = nodeCopies.get(cur.next, None)
            curCpy.random = nodeCopies.get(cur.random, None)

            cur = cur.next

        return nodeCopies[head]
        

        
       