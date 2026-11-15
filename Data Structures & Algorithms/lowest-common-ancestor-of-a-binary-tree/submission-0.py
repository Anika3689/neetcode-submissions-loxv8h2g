# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p == root or q == root:
            return root
        
        lFound = self.lowestCommonAncestor(root.left, p, q)
        rFound = self.lowestCommonAncestor(root.right, p, q)

        if lFound and rFound:
            return root
        if lFound:
            return lFound
    
        return rFound
        