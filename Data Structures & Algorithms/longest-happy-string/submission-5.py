class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        remainingCounts = []
        if a > 0:
            remainingCounts.append((-a, 'a'))
        if b > 0:
            remainingCounts.append((-b, 'b'))
        if c > 0:
            remainingCounts.append((-c, 'c'))

        heapq.heapify(remainingCounts)
        res = []

        while remainingCounts:
            highestCount, mostRemainingLetter = heapq.heappop(remainingCounts)
            if len(res) >= 2 and mostRemainingLetter == res[-1] == res[-2]:
                if not remainingCounts:
                    break
                secondHighestCount, secondRemainingLetter = heapq.heappop(remainingCounts)
                res.append(secondRemainingLetter)

                if secondHighestCount + 1 < 0:
                    heapq.heappush(remainingCounts, (secondHighestCount + 1, secondRemainingLetter))
                
                heapq.heappush(remainingCounts, (highestCount, mostRemainingLetter))
            else:
                res.append(mostRemainingLetter)
                if highestCount + 1 < 0:
                    heapq.heappush(remainingCounts, (highestCount + 1, mostRemainingLetter))
        
        return ''.join(res)