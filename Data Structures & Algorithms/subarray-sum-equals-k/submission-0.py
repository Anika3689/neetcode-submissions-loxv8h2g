class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        countMap = defaultdict(int)
        countMap[0] = 1
        prefixSum = 0
        numSubs = 0
        for num in nums:
            prefixSum += num
            numSubs += countMap[prefixSum - k]
            countMap[prefixSum] += 1
        
        return numSubs