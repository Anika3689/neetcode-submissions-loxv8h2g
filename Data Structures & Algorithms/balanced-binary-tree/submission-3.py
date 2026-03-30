# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def height(cur: TreeNode):
            nonlocal balanced
            if cur is None:
                return -1

            lhs_height = height(cur.left)
            rhs_height = height(cur.right)
            tree_height = max(lhs_height, rhs_height) + 1
            
            if balanced and abs(lhs_height - rhs_height) <= 1:
                return tree_height

            balanced = False
            return tree_height

        height(root)
        return balanced

        
