class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        midpt = len(nums) // 2
        return nums[midpt]