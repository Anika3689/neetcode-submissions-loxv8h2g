class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
                
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                if k < len(nums) - 1 and nums[k] == nums[k+1]:
                    k -= 1
                    continue
                
                summ = nums[j] + nums[k]
                if summ == -nums[i]:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif summ < -nums[i]:
                    j += 1
                else:
                    k -= 1

            i += 1

        return res
