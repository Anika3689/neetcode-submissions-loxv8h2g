class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        amountPerGroup = total // k
        if max(nums) > amountPerGroup:
            return False

        subsets = [0 for _ in range(k)]
        def group(elemIndex):
            if elemIndex == len(nums):
                return all(subset == amountPerGroup for subset in subsets)
            
            for i in range(k):
                if nums[elemIndex] + subsets[i] > amountPerGroup:
                    continue
                if i > 0 and subsets[i] == subsets[i - 1]:
                    continue

                subsets[i] += nums[elemIndex]
                if group(elemIndex + 1):
                    return True
                subsets[i] -= nums[elemIndex]
            
            return False

        nums.sort(reverse=True)
        result = group(0)
        return result





