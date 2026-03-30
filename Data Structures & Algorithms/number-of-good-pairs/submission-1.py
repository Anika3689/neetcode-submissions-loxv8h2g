class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        numGoodPairs = 0
        for num in counts:
            n = counts[num]
            numGoodPairs += (n ** 2 - n) // 2
        
        return numGoodPairs