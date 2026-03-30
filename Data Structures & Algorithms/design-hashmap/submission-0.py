class KeyNode:
    def __init__(self, key: int, val: int, nextNode=None):
        self.key = key
        self.val = val
        self.nextNode = nextNode

class MyHashMap:
    def __init__(self):
        self.hashedMap = [None for _ in range(1009)]
        self.hash_func = lambda key : key % len(self.hashedMap)

    def put(self, key: int, value: int) -> None:
        prev, cur = self._getKeyNode(key)
        if cur:
            cur.val = value
            return
        idx = self.hash_func(key)
        curBucketHead = self.hashedMap[idx]
        self.hashedMap[idx] = KeyNode(key, value, curBucketHead)
        
    def get(self, key: int) -> int:
        prev, cur = self._getKeyNode(key)
        if not cur:
            return -1
        return cur.val

    def _getKeyNode(self, key: int) -> tuple[KeyNode, KeyNode]:
        idx = self.hash_func(key)
        head = self.hashedMap[idx]
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
            self.hashedMap[idx] = cur.nextNode
        else:
            prev.nextNode = cur.nextNode


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)