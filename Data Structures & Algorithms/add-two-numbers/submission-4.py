# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        carry = 0
        while l1 or l2:
            partialSum = carry
            if l1:
                partialSum += l1.val
                l1 = l1.next
            if l2:
                partialSum += l2.val
                l2 = l2.next

            carry = partialSum // 10
            res.next = ListNode(partialSum % 10)
            res = res.next

        if carry:
            res.next = ListNode(carry)
        return dummy.next


        

