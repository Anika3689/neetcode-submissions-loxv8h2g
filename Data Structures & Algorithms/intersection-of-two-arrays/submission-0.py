class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        nums1Elems = set(nums1)
        for elem in nums2:
            if elem in nums1Elems:
                res.add(elem)
        
        return list(res)