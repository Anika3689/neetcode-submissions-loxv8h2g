class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] % 2 == 0 and nums[r] % 2 == 1:
                # left is even, right is odd
                l += 1
                r -= 1
            elif nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r -= 1
            elif nums[l] % 2 == 1:
                # left elem is odd
                nums[r], nums[l] = nums[l], nums[r]
                r -= 1
            else:
                # right elem is even
                nums[r], nums[l] = nums[l], nums[r]
                l += 1

        return nums
