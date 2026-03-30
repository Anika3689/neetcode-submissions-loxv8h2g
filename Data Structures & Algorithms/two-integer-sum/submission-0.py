class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_complements = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in all_complements:
                return [all_complements[nums[i]], i]
            all_complements[complement] = i
          
        

            
