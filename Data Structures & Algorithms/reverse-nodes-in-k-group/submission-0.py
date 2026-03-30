# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def read_next_k_nodes(self, cur):
        i = 1
        while cur and i < self.k:
            cur = cur.next
            i += 1
        return cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.k = k
        prevGroupTail = None
        nextGroupHead = None
        
        numGroup = 1
        cur = head
        while cur:
            cur_cpy = cur
            lastGroupNode = self.read_next_k_nodes(cur_cpy)
            head = lastGroupNode if numGroup == 1 else head
            if lastGroupNode is None:
                prevGroupTail.next = cur
                return head
            nextGroupHead = lastGroupNode.next
            numGroup += 1

            if prevGroupTail: 
                prevGroupTail.next = lastGroupNode
            prevGroupTail = cur
            
            # Reverse nodes in this group:
            prev = None
            while cur != nextGroupHead:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

        return head
    







