class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqs = defaultdict(int)
        times = len(nums) // 3
        for num in nums:
            freqs[num] += 1
        
        res = []
        for num in freqs:
            if freqs[num] > times:
                res.append(num)
        
        return res