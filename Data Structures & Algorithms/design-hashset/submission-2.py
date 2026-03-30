class KeyNode:
    def __init__(self, key: int, nextNode=None):
        self.key = key
        self.nextNode = nextNode
        
class MyHashSet:
    # Problem constraint: Keys are always non-negative!
    def __init__(self):
        self.maxKey = 10 ** 6
        self.n = 10
        self.hashedSet = [None for _ in range(1000)]
        self.hash_func = lambda key : key % len(self.hashedSet)

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        idx = self.hash_func(key)
        curBucketHead = self.hashedSet[idx]
        self.hashedSet[idx] = KeyNode(key, curBucketHead)

    def _getKeyNode(self, key: int) -> tuple[KeyNode, KeyNode]:
        idx = self.hash_func(key)
        head = self.hashedSet[idx]
        if head is None:
            return None, None

        prev = None
        cur = head
        while cur and cur.key != key:
            prev = cur
            cur = cur.nextNode
        return prev, cur

    def remove(self, key: int) -> None:
        prev, cur = self._getKeyNode(key)
        if not cur:
            return
        
        if not prev:
            idx = self.hash_func(key)
            self.hashedSet[idx] = cur.nextNode
        else:
            prev.nextNode = cur.nextNode

    def contains(self, key: int) -> bool:
        prev, cur = self._getKeyNode(key)
        if cur:
            return True
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)