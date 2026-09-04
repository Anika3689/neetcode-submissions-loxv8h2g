class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        h = sum(nums)

        if k == 1:
            return h
        
        def valid(nums, largestSumTarget, k):
            """finds the largest partition sum that is <= largestSumTarget"""
            largestSum = 0
            curSum = 0
            k -= 1
            for num in nums:
                if curSum + num > largestSumTarget:
                    largestSum = max(largestSum, curSum)
                    curSum = num
                    k -= 1
                else:
                    curSum += num

            largestSum = max(largestSum, curSum)
            if k >= 0 and largestSum <= largestSumTarget:
                return True, largestSum
            return False, None
            

        minimized = h
        while l <= h:
            mid = (l + h) // 2
            isValid, foundLargestSum = valid(nums, mid, k)
            if isValid:
                minimized = foundLargestSum
                h = mid - 1
            else:
                l = mid + 1
        
        return minimized
