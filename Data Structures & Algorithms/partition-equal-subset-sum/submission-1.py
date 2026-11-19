class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        target = total // 2
        if n == 1 or total % 2 != 0 or max(nums) > target:
            return False
        
        subsetSums = [[False for _ in range(target + 1)] for _ in range(n+1)]
        for i in range(0, n+1):
            subsetSums[i][target] = True
        
        for i in range(n-1, -1, -1):
            for j in range(target-1, -1, -1):
                if j + nums[i] > target:
                    subsetSums[i][j] = subsetSums[i+1][j]
                else:
                    subsetSums[i][j] = subsetSums[i+1][j] or subsetSums[i+1][j+nums[i]]

        return subsetSums[0][0]

        


