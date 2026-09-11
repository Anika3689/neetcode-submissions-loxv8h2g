# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                tail.next = cur1
                tail = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                tail = cur2
                cur2 = cur2.next
        
        if cur1:
            tail.next = cur1
        elif cur2:
            tail.next = cur2

        return dummy.next
        

            