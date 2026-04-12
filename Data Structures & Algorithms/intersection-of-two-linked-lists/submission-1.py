# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = defaultdict(set)
        cur = headA
        while cur:
            nodes[cur.val].add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in nodes[cur.val]:
                return cur
            cur = cur.next
        
        return None