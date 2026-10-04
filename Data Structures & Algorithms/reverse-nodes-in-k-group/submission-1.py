# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def countNodes(self, head):
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        return count

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.countNodes(head)
        dummy = ListNode(0, head)
        prevGroupTail = dummy
        prev = dummy
        cur = head

        i = 0
        totalCt = 0
        while cur:
            totalCt += 1
            i += 1
            if i == 1:
                curGroupTail = cur
            if i == k:
                prevGroupTail.next = cur
                prevGroupTail = curGroupTail
                i = 0

            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

            if i == 0 and n - totalCt < k:
                prevGroupTail.next = cur
                break

        return dummy.next




