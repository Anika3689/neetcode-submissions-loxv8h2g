# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        counter = 0 #used as a tie-breaker between items with same val
        for lstHead in lists:
            if not lstHead:
                continue
            heapq.heappush(minHeap, (lstHead.val, counter, lstHead))
            counter += 1

        dummyHead = ListNode()
        resTail = dummyHead
        while minHeap:
            smallestVal, _, smallestNode = heapq.heappop(minHeap)
            resTail.next = smallestNode
            resTail = resTail.next

            nextNode = smallestNode.next
            if nextNode:
                heapq.heappush(minHeap, (nextNode.val, counter, nextNode))
                counter += 1
        
        return dummyHead.next