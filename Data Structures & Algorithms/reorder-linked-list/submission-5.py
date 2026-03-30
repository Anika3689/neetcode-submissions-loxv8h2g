# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        lastHalfReversed = self.reverseList(slow.next)
        slow.next = None
        head1 = head
        head2 = lastHalfReversed

        while head1 and head2:
            nextHead1 = head1.next
            head1.next = head2
            nextHead2 = head2.next
            head2.next = nextHead1
            
            head1 = nextHead1
            head2 = nextHead2
        

        
            

        