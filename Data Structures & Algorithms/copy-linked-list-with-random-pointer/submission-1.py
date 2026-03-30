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
            return None
        deep_copies = {}
        cur = head
        prev = None
        while cur:
            new_node = Node(cur.val, None, cur.random)
            if prev:
                prev.next = new_node
            else:
                new_head = new_node
            prev = new_node
            deep_copies[cur] = new_node
            cur = cur.next
        
        cur = head
        while cur:
            node_copy = deep_copies[cur]
            node_copy.random = deep_copies.get(node_copy.random)
            cur = cur.next

        return deep_copies[head]




        