class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.topK = []
        for num in nums:
            if len(self.topK) < k:
                heapq.heappush(self.topK, num)
            elif num > self.topK[0]:
                heapq.heapreplace(self.topK, num)

    def add(self, val: int) -> int:
        if len(self.topK) < self.k:
            heapq.heappush(self.topK, val)
            
        elif val > self.topK[0]:
            heapq.heapreplace(self.topK, val)
        return self.topK[0]

