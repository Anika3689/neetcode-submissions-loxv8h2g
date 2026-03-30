class Solution:
    def reverse(self, nums, l, u):
        """Reverses the array between indices i and j"""
        while l < u:
            curLower = nums[l]
            nums[l] = nums[u]
            nums[u] = curLower
            l += 1
            u -= 1
        return nums


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        return nums
        