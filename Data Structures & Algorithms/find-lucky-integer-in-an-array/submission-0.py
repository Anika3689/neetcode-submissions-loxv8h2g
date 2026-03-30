class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxLuckyCount = 0

        arr.sort()
        i = len(arr) - 1
        while i >= 0:
            curNum = arr[i]
            count = 0
            while i >= 0 and arr[i] == curNum:
                count += 1
                i -= 1
            
            if count == curNum:
                maxLuckyCount = max(count, maxLuckyCount)
        
        return maxLuckyCount if maxLuckyCount > 0 else -1

