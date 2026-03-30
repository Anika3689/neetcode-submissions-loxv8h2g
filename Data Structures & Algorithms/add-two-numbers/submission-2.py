# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getNodeVal(self, node: ListNode):
        if not node:
            return 0
        return node.val

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l1_len, l2_len = 0, 0
        prev_l1, prev_l2 = None, None
        cur_1, cur_2 = l1, l2
        while cur_1 or cur_2:
            total = self.getNodeVal(cur_1) + self.getNodeVal(cur_2) + carry
            digit = total % 10
            carry = total // 10
            if cur_1:
                cur_1.val = digit
                l1_len += 1
                prev_l1 = cur_1
                cur_1 = cur_1.next
            if cur_2:
                cur_2.val = digit
                l2_len += 1
                prev_l2 = cur_2
                cur_2 = cur_2.next

        if l1_len > l2_len:
            if carry:
                prev_l1.next = ListNode(carry)
            return l1
        else:
            if carry:
                prev_l2.next = ListNode(carry)
            return l2
    


        