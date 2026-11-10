# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(cur):
            nonlocal diameter
            if not cur:
                return -1
            
            lHeight = height(cur.left)
            rHeight = height(cur.right)
            diameter = max(lHeight + rHeight + 2, diameter)
            return 1 + max(lHeight, rHeight)
        
        height(root)
        return diameter