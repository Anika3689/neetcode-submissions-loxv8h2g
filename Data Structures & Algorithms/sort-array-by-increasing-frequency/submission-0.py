class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        nums.sort(key=lambda num : (freqs[num], -num))
        return nums