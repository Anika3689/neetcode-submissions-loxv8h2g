class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.lruNode = None
        self.mruNode = None
        self.pointers = {}
    
    def _deleteNode(self, key: int):
        node = self.pointers[key]
        if not node.right:
            self.mruNode = node.left

        if node.left:
            node.left.right = node.right
            if node.right:
                node.right.left = node.left
        else:
            # deleting the head of ordering list
            self.lruNode = self.lruNode.right
            if self.lruNode:
                self.lruNode.left = None

    def get(self, key: int) -> int:
        if key in self.cache:
            self._updateOrdering(key)
            return self.cache.get(key, -1)
        else:
            return -1

    def _updateOrdering(self, key: int) -> None:
        if key in self.pointers:
            self._deleteNode(key)
        
        newMruNode = Node(key, self.mruNode, None)
        if self.mruNode:
            self.mruNode.right = newMruNode
        self.mruNode = newMruNode
        self.pointers[key] = self.mruNode
        if len(self.pointers) == 1:
            self.lruNode = self.mruNode

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) + 1 > self.cap:
            lruKey = self.lruNode.val
            self.cache.pop(lruKey)
            self._deleteNode(lruKey)
            self.pointers.pop(lruKey)
        
        self._updateOrdering(key)
        self.cache[key] = value


            
        

    