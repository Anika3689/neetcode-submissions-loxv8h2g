class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        n = len(nums) / 2
        pairs = 0
        for num in counts:
            if counts[num] % 2 != 0:
                return False
        
        return True