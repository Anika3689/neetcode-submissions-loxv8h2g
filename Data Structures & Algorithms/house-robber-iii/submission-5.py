# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DP Solution
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            if root.left is None and root.right is None:
                return root.val, 0

            take_left, skip_left = dfs(root.left)
            take_right, skip_right = dfs(root.right)

            # Take this house:
            max_take = root.val + skip_left + skip_right
            # Skip this house:
            left_option = max(take_left, skip_left)
            right_option = max(take_right, skip_right)
            max_skip = left_option + right_option

            return max_take, max_skip

        max_take, max_skip = dfs(root)
        return max(max_take, max_skip)




    # # Recursive solution (no caching)
    # def rob(self, root: Optional[TreeNode]) -> int:

    #     def findMaxPathSum(curHouse: TreeNode):
    #         if not curHouse:
    #             return 0
    #         if not (curHouse.left or curHouse.right):
    #             return curHouse.val
            
    #         maxSum = 0
    #         # Rob this house:
    #         children = [curHouse.left, curHouse.right]
    #         maxSum += curHouse.val
    #         for dir_child in children:
    #             if dir_child is None:
    #                 continue
    #             maxSum += findMaxPathSum(dir_child.left)
    #             maxSum += findMaxPathSum(dir_child.right)
            
    #         # Skip this house:
    #         leftPicked = findMaxPathSum(curHouse.left)
    #         rightPicked = findMaxPathSum(curHouse.right)
    #         maxSum = max(maxSum, leftPicked + rightPicked)
    #         return maxSum

    #     return findMaxPathSum(root)




