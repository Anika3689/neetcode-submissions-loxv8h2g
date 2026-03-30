# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, maxPathVal=None) -> int:
        if root is None:
            return 0

        if maxPathVal is None:
            maxPathVal = root.val
        
        numGoodNodes = 0
        if root.val >= maxPathVal:
            numGoodNodes += 1

        maxPathVal = max(root.val, maxPathVal)
        leftGoodNodes = self.goodNodes(root.left, maxPathVal)
        rightGoodNods = self.goodNodes(root.right, maxPathVal)
        numGoodNodes += (leftGoodNodes + rightGoodNods)
        return numGoodNodes