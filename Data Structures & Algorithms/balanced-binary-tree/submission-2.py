# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(cur: TreeNode):
            if cur is None:
                return True, -1

            lhs_balanced, lhs_height = dfs(cur.left)
            rhs_balanced, rhs_height = dfs(cur.right)
            tree_height = max(lhs_height, rhs_height) + 1
            
            if lhs_balanced and rhs_balanced and abs(lhs_height - rhs_height) <= 1:
                return True, tree_height

            return False, tree_height

        is_balanced, height = dfs(root)
        return is_balanced

        
