# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(cur):
            nonlocal k
            if not cur:
                return None
            
            if (kthVal := inorder(cur.left)) is not None:
                return kthVal
            
            k -= 1
            if k == 0:
                return cur.val
            
            if (kthVal := inorder(cur.right)) is not None:
                return kthVal
            
        
        kthVal = inorder(root)
        return kthVal