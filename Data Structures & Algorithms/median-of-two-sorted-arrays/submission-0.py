class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        odd = (m + n) % 2 != 0
        midpoint = (m + n) // 2
        curNum, prevNum = None, None
        i, j = 0, 0

        while i < m and j < n:
            prevNum = curNum
            if nums1[i] <= nums2[j]:
                curNum = nums1[i]  
                i += 1
            else:
                curNum = nums2[j]
                j += 1

            midpoint -= 1
            if midpoint < 0:
                return curNum if odd else (curNum + prevNum) / 2

        if i == m:
            while midpoint >= 0:
                prevNum = curNum
                curNum = nums2[j]
                j += 1
                midpoint -= 1
        elif j == n:
            while midpoint >= 0:
                prevNum = curNum
                curNum = nums1[i]
                i += 1
                midpoint -= 1
            
        return curNum if odd else (curNum + prevNum) / 2


