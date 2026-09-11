# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur != None:
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp 
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = None
        slow = head 
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = None
        else:
            return
        head2 = self.reverseList(slow)
        dummy = ListNode()
        tail = dummy

        while head and head2:
            tail.next = head
            temp = head.next
            head.next = head2

            head = temp
            tail = head2
            head2 = head2.next
        



        
        

