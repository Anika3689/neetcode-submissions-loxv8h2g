class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorElem = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == majorElem:
                count += 1
            else:
                count -= 1
            
            if count == -1:
                majorElem = nums[i]
                count = 1
        
        return majorElem


    # Solution with sorting: o(nlogn)
    # def majorityElement(self, nums: List[int]) -> int:
    #     nums.sort()
    #     midpt = len(nums) // 2
    #     return nums[midpt]