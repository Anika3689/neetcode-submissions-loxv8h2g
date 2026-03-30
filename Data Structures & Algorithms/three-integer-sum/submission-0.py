class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()

        for i in range(len(nums)):
            remainder = 0 - nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                potentialRem = nums[left] + nums[right]
                
                if potentialRem == remainder:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif potentialRem < remainder:
                    left += 1
                else:
                    right -= 1
        
        result = []
        for triple in triplets:
            result.append(list(triple))
        return result
    