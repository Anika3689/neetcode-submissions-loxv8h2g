# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        stk = [root]
        while stk:
            curNode = stk.pop()
            res.append(curNode.val)
            if curNode.right:
                stk.append(curNode.right)
            if curNode.left:
                stk.append(curNode.left)
        
        return res





        # def dfs(cur: TreeNode, res: list):
        #     if not cur:
        #         return
        #     res.append(cur.val)
        #     dfs(cur.left, res)
        #     dfs(cur.right, res)
        
        # res = []
        # dfs(root, res)
        # return res