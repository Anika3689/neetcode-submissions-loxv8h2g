class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        def helper(nums, i, j):
            if i == j:
                return nums[i], 1

            midpt = (i + j) // 2
            lhsMajorElem, lhsMajorExcess = helper(nums, i, midpt)
            rhsMajorElem, rhsMajorExcess = helper(nums, midpt + 1, j)

            if lhsMajorElem == rhsMajorElem:
                return lhsMajorElem, lhsMajorExcess + rhsMajorExcess

            if lhsMajorExcess > rhsMajorExcess:
                return lhsMajorElem, lhsMajorExcess - rhsMajorExcess

            return rhsMajorElem, rhsMajorExcess - lhsMajorExcess
        
        majorElem, _ = helper(nums, 0, len(nums) - 1) 
        return majorElem



    # Solution with sorting: o(nlogn)
    # def majorityElement(self, nums: List[int]) -> int:
    #     nums.sort()
    #     midpt = len(nums) // 2
    #     return nums[midpt]