# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        globalMaxSum = root.val
        
        #Returns the maximum path sum going through root
        def dfs(root):
            nonlocal globalMaxSum
            if not root:
                return 0

            leftPathMaxSum = max(0, dfs(root.left))
            rightPathMaxSum = max(0, dfs(root.right))

            sumThroughRoot = leftPathMaxSum + root.val + rightPathMaxSum 
            leftPathMaxSum += root.val 
            rightPathMaxSum += root.val 
            
            maxWithRoot = max(sumThroughRoot, leftPathMaxSum, rightPathMaxSum)
            globalMaxSum = max(globalMaxSum, maxWithRoot)

            return max(leftPathMaxSum, rightPathMaxSum)
            
        dfs(root)
        return globalMaxSum
        
