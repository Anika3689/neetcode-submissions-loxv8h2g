class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        studentCount = len(nums)
        r = k-1 if studentCount >= k else studentCount - 1
        bestMinDiff = nums[r] - nums[0]
        for l in range(1, studentCount - k + 1):
            r += 1
            bestMinDiff = min(nums[r] - nums[l], bestMinDiff)
            
        return bestMinDiff
