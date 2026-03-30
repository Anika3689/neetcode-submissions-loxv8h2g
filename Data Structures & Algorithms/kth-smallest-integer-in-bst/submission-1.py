# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth_val = None
        cnt = 0
        def inorder(root):
            nonlocal kth_val, cnt
            if not root:
                return
            inorder(root.left)
            cnt += 1
            if cnt == k:
                kth_val = root.val
            inorder(root.right)

        inorder(root)
        return kth_val





        
