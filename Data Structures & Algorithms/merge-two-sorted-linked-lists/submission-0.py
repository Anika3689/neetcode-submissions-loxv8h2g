# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy_head = ListNode()
        res_tail = dummy_head

        while list1 and list2:
            if list1.val <= list2.val:
                res_tail.next = list1
                res_tail = list1
                list1 = list1.next
            else:
                res_tail.next = list2
                res_tail = list2
                list2 = list2.next

        if list1:
            res_tail.next = list1
        if list2:
            res_tail.next = list2
        
        return dummy_head.next

