class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Indices = {elem : i for i, elem in enumerate(nums2)}
        decStack = [0]
        for i in range(1, len(nums2)):
            curElem = nums2[i]
            while decStack and curElem > nums2[decStack[-1]]:
                topIndex = decStack.pop()
                nums2[topIndex] = curElem
            
            decStack.append(i)

        while decStack:
            index = decStack.pop()
            nums2[index] = -1

        res = [nums2[nums2Indices[elem]] for elem in nums1]
        return res
        

            
            

