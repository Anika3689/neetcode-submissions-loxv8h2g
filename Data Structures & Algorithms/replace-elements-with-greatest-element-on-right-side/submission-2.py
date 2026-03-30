class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = -1
        for i in range(len(arr) - 1, -1, -1):
            curVal = arr[i]
            arr[i] = maxVal
            maxVal = max(curVal, maxVal)
        
        return arr