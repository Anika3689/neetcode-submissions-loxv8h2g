class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        numTrees = len(fruits)
        fruitCounts = defaultdict(int)
        maxPicked = 0
        l = 0
        for r in range(numTrees):
            fruitCounts[fruits[r]] += 1

            while l < numTrees and len(fruitCounts) > 2:
                fruitType = fruits[l]
                fruitCounts[fruitType] -= 1
                if fruitCounts[fruitType] <= 0:
                    fruitCounts.pop(fruitType)
                l += 1
            
            curPicked = r - l + 1
            maxPicked = max(maxPicked, curPicked)
        

        return maxPicked
