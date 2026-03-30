# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = head
        cur = prev.next
        while cur:
            next_node = cur.next
            cur.next = prev

            prev = cur
            cur = next_node
        head.next = None
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = None
        slow = head
        fast = head
        # Move slow pointer to the middle of the list
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if not prev:
            return None
        prev.next = None
        sec_half = self.reverseList(slow)
        
        # Pair corresponding nodes in first and second half
        first_half = head
        prev = None
        while first_half and sec_half:
            next_node_first = first_half.next
            next_node_sec = sec_half.next

            first_half.next = sec_half
            sec_half.next = next_node_first

            prev = sec_half
            first_half = next_node_first
            sec_half = next_node_sec
        
        if sec_half:
            prev.next = sec_half


        

        
        








