# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = defaultdict(list)
        cur = headA
        while cur:
            nodes[cur.val].append(cur)
            cur = cur.next
        cur = headB
        while cur:
            for node in nodes[cur.val]:
                if cur == node:
                    return cur
            cur = cur.next
        
        return None