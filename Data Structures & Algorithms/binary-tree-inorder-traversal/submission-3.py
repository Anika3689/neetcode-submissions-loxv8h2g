# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(cur: TreeNode, res=None):
            if not cur:
                return
            
            dfs(cur.left, res)
            res.append(cur.val)
            dfs(cur.right, res)

        res = []
        dfs(root, res)
        return res

        
