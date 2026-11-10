# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            res.append([])
            nextLevel = []
            while q:
                front = q.popleft()
                res[-1].append(front.val)
                if front.left:
                    nextLevel.append(front.left)
                if front.right:
                    nextLevel.append(front.right)

            for node in nextLevel:
                q.append(node)

        return res