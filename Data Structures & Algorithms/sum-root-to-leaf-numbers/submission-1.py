# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, curPath: list[int]):
            nonlocal totalSum
            if not root:
                return
            curPath.append(root.val)
            if not (root.left or root.right):
                nDigits = len(curPath)
                number = sum(curPath[i] * 10**(nDigits-i-1) for i in range(nDigits))
                totalSum += number

            dfs(root.left, curPath)
            dfs(root.right, curPath)
            curPath.pop()

        totalSum = 0
        curPath = []
        dfs(root, curPath)
        return totalSum