# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node_to_insert = TreeNode(val)
        if root is None:
            return node_to_insert

        cur = root
        prev = None
        while cur:
            prev = cur
            if val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        
        if val > prev.val:
            prev.right = node_to_insert
        else:
            prev.left = node_to_insert
        
        return root
