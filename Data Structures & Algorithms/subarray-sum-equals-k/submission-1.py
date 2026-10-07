class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumCounts = {0 : 1}
        prefixSums = [0] * len(nums)
        numSubs = 0
        
        for i in range(len(nums)):
            if i == 0:
                prefixSums[i] = nums[i]
            else:
                prefixSums[i] = nums[i] + prefixSums[i-1]

            remove = prefixSums[i] - k
            numSubs += sumCounts.get(remove, 0)
            sumCounts[prefixSums[i]] = sumCounts.get(prefixSums[i], 0) + 1
        
        return numSubs