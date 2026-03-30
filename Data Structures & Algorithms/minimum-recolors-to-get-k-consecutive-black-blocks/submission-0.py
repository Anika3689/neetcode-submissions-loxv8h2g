class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        numBlocks = len(blocks)
        minRecolors = 0
        for i in range(k):
            if blocks[i] == 'B':
                continue
            minRecolors += 1
        
        curWhites = minRecolors
        for l in range(1, numBlocks - k + 1):
            r = l + k - 1
            if blocks[r] == 'W':
                curWhites += 1
            if blocks[l - 1] == 'W':
                curWhites -= 1
            
            minRecolors = min(minRecolors, curWhites)
        
        return minRecolors