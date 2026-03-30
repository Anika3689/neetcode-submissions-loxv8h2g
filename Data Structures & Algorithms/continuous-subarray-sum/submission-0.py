class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderCounts = defaultdict(list)
        remainderCounts[0] = [-1]
        curSum = 0
        for i, num in enumerate(nums):
            curSum += num
            indicesPrevMultiples = remainderCounts[curSum % k]
            for idx in indicesPrevMultiples:
                if i - idx >= 2:
                    return True
            remainderCounts[curSum % k].append(i)

        return False