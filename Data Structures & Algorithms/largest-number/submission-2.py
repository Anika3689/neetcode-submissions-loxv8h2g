from functools import cmp_to_key
class Solution:
    """
    < 0   if a should come before b
    = 0   if equal
    > 0   if a should come after b
    """
    def cmp(a, b):
        a_first = a + b
        b_first = b + a
        
        if a_first > b_first:
            return -1
        elif a_first < b_first:
            return 1  
        return 0

    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return '0'
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(Solution.cmp))
        return ''.join(nums)






