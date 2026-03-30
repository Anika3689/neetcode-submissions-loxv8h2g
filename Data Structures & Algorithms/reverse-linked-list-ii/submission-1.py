# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy_head = ListNode(0, head)
        cur = dummy_head
        i = 0
        while cur and i < left - 1:
            cur = cur.next
            i += 1
        leftGroupTail = cur
        prev = cur
        leftNode = cur.next
        cur = cur.next
        i += 1
        while cur and i <= right:
            temp = cur.next 
            cur.next = prev
            prev = cur
            cur = temp
            i += 1

        rightGroupHead = cur
        leftGroupTail.next = prev
        leftNode.next = rightGroupHead

        return dummy_head.next

