class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        freqs = defaultdict(int)
        freq_buckets = [[] for _ in range(n)]
        for num in nums:
            freqs[num] += 1
        
        for elem in freqs:
            freq = freqs[elem]
            freq_buckets[freq - 1].append(elem)
        
        topK = []
        kRemaining = k

        for i in range(n-1, -1, -1):
            if len(freq_buckets[i]) >= kRemaining:
                topK += (freq_buckets[i])[:kRemaining]
                break
            else:
                topK += freq_buckets[i]
                kRemaining -= len(freq_buckets[i])
        
        return topK


