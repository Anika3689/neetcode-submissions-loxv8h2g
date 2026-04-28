class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = [(-count, ch) for ch, count in Counter(s).items()]
        heapq.heapify(counts)
        # early checking if rearrangement is not possible
        if len(s) % 2 == 0 and -counts[0][0] > len(s) / 2:
            return ""
        if len(s) % 2 != 0 and -counts[0][0] > 1 + len(s) // 2 :
            return ""

        res = [None for _ in range(len(s))]
        i = 0
        unusable = () # (character, remaining count)
        while counts:
            maxCount, maxChar = heapq.heappop(counts)
            res[i] = maxChar
            i += 1

            if unusable and unusable[1] < 0:
                heapq.heappush(counts, (unusable[1], unusable[0]))

            unusable = (maxChar, maxCount + 1)

        return ''.join(res)
