# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        i = 1
        lhs = dummy
        cur = head

        while i < left:
            lhs = cur
            cur = cur.next
            i += 1
        
        newTail = cur
        prev = None
        
        while i <= right:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
            i += 1

        lhs.next = prev
        newTail.next = cur

        return dummy.next


        
        
        

        

