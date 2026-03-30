class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Mapping = {num : i for i, num in enumerate(nums2)}
        indexMapping = []
        for i in range(len(nums1)):
            num1 = nums1[i]
            indexMapping.append(nums2Mapping[num1])
        
        return indexMapping