class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        allPerms = []

        def helper(curPerm, counts):
            if len(curPerm) == len(nums):
                allPerms.append(curPerm.copy())
                return
            
            for num in counts:
                if counts[num] <= 0:
                    continue
                curPerm.append(num)
                counts[num] -= 1
                helper(curPerm, counts)
                curPerm.pop()
                counts[num] += 1

        curPerm = []
        counts = Counter(nums)
        helper(curPerm, counts)
        return allPerms