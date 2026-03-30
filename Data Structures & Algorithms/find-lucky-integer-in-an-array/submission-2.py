class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        i = len(arr) - 1
        while i >= 0:
            curNum = arr[i]
            count = 0
            while i >= 0 and arr[i] == curNum:
                count += 1
                i -= 1
            
            if count == curNum:
                return count
        
        return -1

