# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def helper(cur):
            if not cur:
                return True, 0
            
            lBalanced, lDepth = helper(cur.left)
            rBalanced, rDepth = helper(cur.right)

            if lBalanced and rBalanced and abs(lDepth - rDepth) <= 1:
                return True, 1 + max(lDepth, rDepth)
            return False, 1 + max(lDepth, rDepth)
        
        balanced, _ = helper(root)
        return balanced