class Node:
    def __init__(self, key, val, l=None, r=None):
        self.key = key
        self.val = val
        self.left = l
        self.right = r

class LRUCache:
    def __init__(self, capacity: int):
        self.nodePointers = {}
        self.cap = capacity
        self.size = 0
        self.leastRecent = None
        self.mostRecent = None

    def _removeNode(self, node) -> None:
        # assumes that key is in cache
        self.size -= 1
        self.nodePointers.pop(node.key)

        if node.left:
            node.left.right = node.right
        else:
            self.leastRecent = node.right

        if node.right:
            node.right.left = node.left 
        else:
            self.mostRecent = node.left

    def _addMostRecentEntry(self, key: int, value: int):
        self.size += 1
        newTail = Node(key, value, self.mostRecent)
        self.nodePointers[key] = newTail

        if self.mostRecent:
            self.mostRecent.right = newTail
        else:
            self.leastRecent = newTail

        self.mostRecent = newTail

    def get(self, key: int) -> int:
        if key not in self.nodePointers:
            return -1
        
        node = self.nodePointers[key]
        value = node.val

        self._removeNode(node)
        self._addMostRecentEntry(key, value)
        
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.nodePointers:
            self._removeNode(self.nodePointers[key])

        self._addMostRecentEntry(key, value)

        if self.size > self.cap:
            self._removeNode(self.leastRecent)


            
        

    