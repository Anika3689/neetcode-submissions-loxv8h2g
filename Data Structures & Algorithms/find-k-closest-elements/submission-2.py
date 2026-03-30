class Solution:
    """Finds the first index greater than (or equal) to x"""
    def searchPosition(self, nums, x):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < x:
                left = mid + 1
            else:
                right = mid
        # while left-1 >= 0 and nums[left-1] == x:
        #     left -= 1
        return left

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[n-1]:
            return arr[n-k:]

        pos = self.searchPosition(arr, x)
        kFound = 0
        if arr[pos] == x:
            kFound += 1
            left, right = pos-1, pos+1
        else:
            left, right = pos-1, pos

        while kFound < k:
            if left < 0:
                right += 1
            elif right > n-1:
                left -= 1
            else:
                leftDist, rightDist = x-arr[left], arr[right]-x
                if leftDist <= rightDist:
                    left -= 1
                else:
                    right += 1

            kFound += 1
        
        return arr[left + 1: right]



            
