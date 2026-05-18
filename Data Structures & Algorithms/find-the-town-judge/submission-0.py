class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusteeCounts = defaultdict(int)
        trusterCounts = defaultdict(int)

        for trustPair in trust:
            truster, trustee = trustPair
            trusteeCounts[trustee] += 1
            trusterCounts[truster] += 1

        judge = None
        for person in range(1, n + 1):
            numTrustees = trusteeCounts[person]
            if numTrustees == n - 1 and trusterCounts[person] == 0:
                if judge:
                    return -1
                judge = person

        return judge if judge else -1

