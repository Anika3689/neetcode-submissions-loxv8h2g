# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best_diameter = 0

        def height(node):
            nonlocal best_diameter
            if node is None:
                return -1
            
            lhs_height = height(node.left)
            rhs_height = height(node.right)
            best_diameter = max(best_diameter, lhs_height + rhs_height + 2)
            return 1 + max(lhs_height, rhs_height)
        
        height(root)
        return best_diameter

