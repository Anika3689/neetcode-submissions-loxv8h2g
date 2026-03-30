class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r and nums[r] == val:
            r -= 1

        while l <= r:
            print(nums)
            if nums[l] == val:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1 
                while l <= r and nums[r] == val:
                    r -= 1
                continue
            
            l += 1
            
        for i in range(len(nums) - 1, r, -1):
            nums.pop()
        
        return r + 1