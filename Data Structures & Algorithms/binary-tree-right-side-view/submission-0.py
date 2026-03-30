# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        res = []
        curLevel = 0
        queue = deque([(root, 0)])
        while queue:
            first_elem, level = queue.popleft()
            if level >= len(res):
                new_level_entry = [first_elem.val]
                res.append(new_level_entry)
            else:
                res[level].append(first_elem.val)

            if first_elem.left:
                queue.append( (first_elem.left, level+1) )
            if first_elem.right:
                queue.append( (first_elem.right, level+1) )

        return res

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_order = self.levelOrder(root)
        rightside_view = []
        for level_nodes in level_order:
            rightside_view.append(level_nodes[-1])
        return rightside_view




        