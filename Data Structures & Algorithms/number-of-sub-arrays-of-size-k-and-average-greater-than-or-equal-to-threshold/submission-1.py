class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        sumThresh = k * threshold

        res = 0
        curSum = 0
        for i in range(k):
            curSum += arr[i]

        if curSum >= sumThresh:
            res += 1
        
        for r in range(k, n):
            curSum -= arr[r - k]
            curSum += arr[r]

            if curSum >= sumThresh:
                res += 1
        
        return res