# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # bounds (minVal, maxVal) are exclusive
    def isValidBST(self, root: Optional[TreeNode], minVal=None, maxVal=None) -> bool:
        if not root:
            return True

        if minVal is None:
            minVal = -1001
        if maxVal is None:
            maxVal = 1001
        
        if not(minVal < root.val < maxVal):
            print(minVal, root.val, maxVal)
            return False
        
        leftIsValid = self.isValidBST(root.left, minVal, root.val)
        rightIsValid = self.isValidBST(root.right, root.val, maxVal)

        return leftIsValid and rightIsValid

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     def helper(root):
    #         if not root:
    #             return True, None, None
    #         if not root.left and not root.right:
    #             return True, root.val, root.val

    #         leftIsValid, leftMaxVal, leftMinVal = helper(root.left)
    #         rightIsValid, rightMaxVal, rightMinVal = helper(root.right)

    #         if not (leftIsValid and rightIsValid):
    #             return False, None, None

    #         # Root must have at least one child:
    #         if not root.left:
    #             treeMinVal = min(root.val, rightMinVal)
    #             treeMaxVal = max(root.val, rightMaxVal)
    #         elif not root.right:
    #             treeMinVal = min(leftMinVal, root.val)
    #             treeMaxVal = max(leftMaxVal, root.val)
    #         else:
    #             treeMinVal = min(leftMinVal, root.val, rightMinVal)
    #             treeMaxVal = max(leftMaxVal, root.val, rightMaxVal)
            
    #         left_cond = leftMaxVal is None or leftMaxVal < root.val 
    #         right_cond = (rightMinVal is None or rightMinVal > root.val)
    #         if left_cond and right_cond:
    #             return True, treeMaxVal, treeMinVal

    #         return False, None, None

        
    #     validStatus, _, _ = helper(root)
    #     return validStatus




