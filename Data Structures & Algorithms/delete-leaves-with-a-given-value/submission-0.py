# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(curNode) -> bool:
            if curNode is None:
                return False
            
            removeChild = dfs(curNode.left)   
            if removeChild:
                curNode.left = None
            removeChild = dfs(curNode.right)
            if removeChild:
                curNode.right = None
            
            if curNode.val == target and not(curNode.left or curNode.right):
                return True
            
            return False

        removeRoot = dfs(root)
        if removeRoot:
            return None
        return root

