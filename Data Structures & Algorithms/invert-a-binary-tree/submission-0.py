# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        
        invertedLeftSub = self.invertTree(root.left)
        invertedRightSub = self.invertTree(root.right)

        root.left = invertedRightSub
        root.right = invertedLeftSub

        return root