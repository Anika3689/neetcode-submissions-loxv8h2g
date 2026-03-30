class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr[-1] = (arr[-1], -1)

        for i in range(len(arr) - 2, -1, -1):
            rightElem, rightMax = arr[i+1]
            arr[i] = (arr[i], max(rightElem, rightMax))
        
        for i in range(len(arr)):
            arr[i] = arr[i][1]
        
        return arr