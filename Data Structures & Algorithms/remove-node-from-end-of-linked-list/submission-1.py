# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        for i in range(n):
            cur = cur.next

        nth_pointer = head
        prev = None
        while cur:
            cur = cur.next
            prev = nth_pointer
            nth_pointer = nth_pointer.next
        
        if not prev:
            return nth_pointer.next
        prev.next = nth_pointer.next
        return head