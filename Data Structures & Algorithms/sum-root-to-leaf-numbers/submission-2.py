# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:  
        def dfs(root, curNum: int):
            nonlocal totalSum
            if not root:
                return
            curNum = curNum * 10 + root.val
            if not (root.left or root.right):
                totalSum += curNum

            dfs(root.left, curNum)
            dfs(root.right, curNum)

        totalSum = 0
        curNum = 0
        dfs(root, curNum)
        return totalSum