class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        numSpots = len(flowerbed)
        for i in range(numSpots):
            if n <= 0:
                return True
            if flowerbed[i] == 1:
                continue
            if (i > 0 and flowerbed[i-1] == 1) or (i < numSpots-1 and flowerbed[i+1] == 1):
                continue
            
            flowerbed[i] = 1
            n -= 1
        
        return n <= 0