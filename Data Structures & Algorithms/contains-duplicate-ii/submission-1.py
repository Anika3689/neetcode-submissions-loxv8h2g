class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # Mapping between values in nums and their most recent index
        indices = {}
        
        for i in range(n):
            num = nums[i]
            if num in indices and i - indices[num] <= k:
                return True
            # update the most recently visited index for this number
            indices[num] = i
        
        return False
        