class MyHashSet:
    # Problem constraint: Keys are always non-negative!
    def __init__(self):
        self.maxKey = 10 ** 6
        self.hashedSet = [False for _ in range(self.maxKey + 1)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.hashedSet[key] = True

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashedSet[key] = False

    def contains(self, key: int) -> bool:
        return self.hashedSet[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)