class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stk = []
        nextGreaterElems = {}

        for j in range(len(nums2)):
            while stk and (prevVal := stk[-1]) < nums2[j]:
                stk.pop()
                nextGreaterElems[prevVal] = nums2[j]

            stk.append(nums2[j])
        
        ans = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            ans[i] = nextGreaterElems.get(num, -1)
        
        return ans