class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        toRemove = set()
        for i in range(1, len(nums)):
            if nums[i] == prev:
                toRemove.add(i)
            else:
                prev = nums[i]
        
        dec = 0
        for removeIdx in toRemove:
            nums.pop(removeIdx - dec)
            dec += 1
        
        return len(nums)
