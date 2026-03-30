class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        quads = []
        for a in range(n):
            if a > 0 and nums[a] == nums[a-1]: #skip duplicate a
                continue
            first = nums[a]
            for b in range(a+1, n):
                if b > a+1 and nums[b] == nums[b-1]:  # skip duplicate b
                    continue
                sec = nums[b]
                remainder = target - (first + sec)
                c = b+1
                d = n-1
                while c < d:
                    third, fourth = nums[c], nums[d]
                    summ = third + fourth 
                    if summ == remainder:
                        quads.append([first, sec, third, fourth])
                        c += 1
                        d -= 1
                        #Skip past duplicate quads
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1   
                    elif summ > remainder:
                        d -= 1
                    else:
                        c += 1
                
        return quads