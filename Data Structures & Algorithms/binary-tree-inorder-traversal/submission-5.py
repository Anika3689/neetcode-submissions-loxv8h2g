# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stk = [[root, False]]
        res = []
        while stk:
            cur, left_visited = stk[-1]
            if cur and cur.left and not left_visited:
                stk[-1][1] = True
                stk.append([cur.left, False])
            elif cur:
                res.append(cur.val)
                stk.pop()
                if cur.right:
                    stk.append([cur.right, False])

        return res

            


        
