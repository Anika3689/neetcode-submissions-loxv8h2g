# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        # Current node is the one to be deleted
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        cur = root.right
        while cur.left:
            cur = cur.left

        cur.left = root.left
        return root.right

    # Iterative version:
    # def searchNode(self, key, root):
    #     cur = root
    #     prev = None
    #     child_direction = None
    #     while cur:
    #         if key == cur.val:
    #             break
    #         prev = cur
    #         if key > cur.val:
    #             cur = cur.right
    #             child_direction = 'right'
    #         else:
    #             cur = cur.left
    #             child_direction = 'left'

    #     return prev, cur, child_direction
        
    # def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    #     if root is None:
    #         return None

    #     parent, deleteNode, child_direction = self.searchNode(key, root)
    #     if deleteNode is None:
    #         return root

    #     if deleteNode != root:
    #         if not deleteNode.right:
    #             if child_direction == 'left':
    #                 parent.left = deleteNode.left
    #             else:
    #                 parent.right = deleteNode.left
    #             return root
    #         if not deleteNode.left:
    #             if child_direction == 'left':
    #                 parent.left = deleteNode.right
    #             else:
    #                 parent.right = deleteNode.right
    #             return root

    #         cur = deleteNode.right
    #         while cur.left:
    #             cur = cur.left
    #         cur.left = deleteNode.left

    #         if child_direction == 'right':
    #             parent.right = deleteNode.right
    #         else:
    #             parent.left = deleteNode.right

    #         return root
    #     else:
    #         if deleteNode.right is None:
    #             return deleteNode.left
            
    #         cur = deleteNode.right
    #         while cur.left:
    #             cur = cur.left
    #         cur.left = deleteNode.left
    #         root = deleteNode.right
    #         return root








