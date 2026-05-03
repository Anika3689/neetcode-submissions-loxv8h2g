class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        originalCounts = {'a' : a, 'b': b, 'c': c}
        remainingCounts = []
        if a > 0:
            remainingCounts.append((-a, 'a'))
        if b > 0:
            remainingCounts.append((-b, 'b'))
        if c > 0:
            remainingCounts.append((-c, 'c'))

        heapq.heapify(remainingCounts)
        res = []
        cooldown = []

        while cooldown or remainingCounts:
            removeFromCooldown = set()
            for i, item in enumerate(cooldown):
                letter, remaining, wait = item
                if wait == 0:
                    heapq.heappush(remainingCounts, (remaining, letter))
                    removeFromCooldown.add(i)
                else:
                    cooldown[i][-1] -= 1

            for i in removeFromCooldown:
                cooldown.pop(i)

            if not remainingCounts:
                break
            remainingOccurences, mostRemainingLetter = heapq.heappop(remainingCounts)
            res.append(mostRemainingLetter)
            if remainingOccurences + 1 < 0:
                if len(res) > 1 and res[-2] == res[-1]:
                    cooldown.append([mostRemainingLetter, remainingOccurences + 1, 1])
                else:
                    heapq.heappush(remainingCounts, (remainingOccurences + 1, mostRemainingLetter))
                
            #print(cooldown)

        return ''.join(res)



