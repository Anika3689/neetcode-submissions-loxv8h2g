class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        resIndex = first = len(nums1) - 1
        first = m - 1
        second = n - 1

        while first >= 0 and second >= 0:
            if nums1[first] >= nums2[second]:
                nums1[resIndex] = nums1[first]
                first -= 1
            else:
                nums1[resIndex] = nums2[second]
                second -= 1
            
            resIndex -= 1
        
        while first >= 0:
            nums1[resIndex] = nums1[first]
            resIndex -= 1
            first -= 1
        while second >= 0:
            nums1[resIndex] = nums2[second]
            resIndex -= 1
            second -= 1
        
        return nums1