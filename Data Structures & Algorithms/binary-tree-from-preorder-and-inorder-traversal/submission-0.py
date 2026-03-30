# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        inorder_indices = {elem : index for index, elem in enumerate(inorder)}

        def treeBuilder(preorder, inorder, l: int, r: int):
            nonlocal preorder_index, inorder_indices
            if preorder_index >= len(preorder) or r < l:
                return None
            
            cur_root = TreeNode(preorder[preorder_index])
            root_index = inorder_indices[preorder[preorder_index]]
            preorder_index += 1
            cur_root.left = treeBuilder(preorder, inorder, l, root_index-1)
            cur_root.right = treeBuilder(preorder, inorder, root_index+1, r)

            return cur_root

        root = treeBuilder(preorder, inorder, 0, len(inorder))
        return root
            