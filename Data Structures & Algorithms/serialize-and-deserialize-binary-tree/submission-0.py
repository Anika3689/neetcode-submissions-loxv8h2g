# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def __init__(self):
        self.delim = ','

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        serialized = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                serialized.append('n')
                continue

            serialized.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)


        return (self.delim).join(serialized)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        stream = data.split(self.delim)
        root = TreeNode(data[0])
        queue = deque([root])
        i = 1
        while i < len(stream):
            curNode = queue.popleft()
            if curNode is None:
                continue
            
            if i < len(stream):
                curNode.left = TreeNode(stream[i]) if stream[i] != 'n' else None
                queue.append(curNode.left)
                i += 1
            if i < len(stream):
                curNode.right = TreeNode(stream[i]) if stream[i] != 'n' else None
                queue.append(curNode.right)
                i += 1

        return root



            





