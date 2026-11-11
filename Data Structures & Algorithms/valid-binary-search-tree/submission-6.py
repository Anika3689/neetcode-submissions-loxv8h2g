# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(cur):
            if not cur:
                return True, None, None
            
            leftValid, leftMin, leftMax = helper(cur.left)
            if not leftValid or (leftMax is not None and leftMax >= cur.val):
                return False, None, None
            rightValid, rightMin, rightMax = helper(cur.right)
            if not rightValid or (rightMin is not None and rightMin <= cur.val):
                return False, None, None
            
            if leftMin is None:
                leftMin = cur.val
            if rightMax is None:
                rightMax = cur.val
            return True, leftMin, rightMax
        
        isValid, _, _ = helper(root)
        return isValid

        
            