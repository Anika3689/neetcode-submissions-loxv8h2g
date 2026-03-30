class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            remainder = 0 - nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                potentialRem = nums[left] + nums[right]
                if potentialRem == remainder:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                            left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif potentialRem < remainder:
                    left += 1
                else:
                    right -= 1
        
        return triplets
    