class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        minOps = 0
        for val in counts:
            count = counts[val]
            if count < 2:
                return -1
            if count % 3 == 0:
                minOps += count // 3
            else:
                minOps += count // 3 + 1
        
        return minOps