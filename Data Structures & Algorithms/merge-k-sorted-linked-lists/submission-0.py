# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def allListsExhausted(self, curHeads: list):
        for head in curHeads:
            if head:
                return False
        return True

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        resHead = None
        res = None
        while not self.allListsExhausted(lists):
            minListIndex = None
            for listIndex, elem in enumerate(lists):
                if not elem:
                    continue
                if minListIndex is None or (elem.val < lists[minListIndex].val):
                    minListIndex = listIndex
            
            if not resHead:
                res = lists[minListIndex]
                resHead = res
            else:
                res.next = lists[minListIndex]
                res = res.next

            lists[minListIndex] = lists[minListIndex].next
        
        return resHead







            

                