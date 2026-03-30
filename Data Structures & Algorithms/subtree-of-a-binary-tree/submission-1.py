# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        lhs_equal = self.isSameTree(p.left, q.left)
        rhs_equal = self.isSameTree(p.right, q.right)

        if lhs_equal and rhs_equal and p.val == q.val:
            return True

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes = deque([root])
        while nodes:
            cur = nodes.pop()
            if self.isSameTree(cur, subRoot):
                return True
            
            if cur.left:
                nodes.append(cur.left)
            if cur.right:
                nodes.append(cur.right)

        return False


        


