class Solution:  

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] < nums[n-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        while right - left >= 2:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            if nums[mid + 1] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            return min(nums[left], nums[right])
         
        #return nums[left]