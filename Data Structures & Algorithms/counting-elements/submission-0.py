class Solution:
    def countElements(self, arr: List[int]) -> int:
        elemCt = 0
        arr.sort()
        n = len(arr)
        i = 0
        while i < n:
            num = arr[i]
            dupCount = 0
            while i < n and arr[i] == num:
                dupCount += 1
                i += 1
            
            if i < n and arr[i] == num + 1:
                elemCt += dupCount 

        return elemCt

