class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-weight for weight in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = abs(stones[0])
            if len(stones) >= 3:
                stone2 = abs(min(stones[1], stones[2]))
            else:
                stone2 = abs(stones[1])

            if stone1 == stone2:
                heapq.heappop(stones)
                heapq.heappop(stones)
                continue
            
            heapq.heappop(stones)
            heapq.heapreplace(stones, -(stone1 - stone2))
        
        if stones:
            return -stones[0]
        return 0
        

            
            

