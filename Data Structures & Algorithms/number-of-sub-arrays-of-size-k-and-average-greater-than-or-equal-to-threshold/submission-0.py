class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        minWindowSum = k * threshold
        numSubs = 0
        curSum = 0
        for i in range(k):
            curSum += arr[i]
        
        if curSum >= minWindowSum:
            numSubs += 1
        
        for l in range(1, len(arr) - k + 1):
            r = l + k - 1
            curSum -= arr[l-1]
            curSum += arr[r]

            if curSum >= minWindowSum:
                numSubs += 1
        
        return numSubs