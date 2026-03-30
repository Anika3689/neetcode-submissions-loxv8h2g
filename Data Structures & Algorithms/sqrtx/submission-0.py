class Solution:

    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        if x == 2 or x == 3:
            return 1
        
        low, high = 2, x // 2
        while low <= high:
            mid = (low + high) // 2
            squared = mid * mid 
            if squared == x:
                return mid
            if squared < x:
                low = mid + 1
            else:
                high = mid - 1

        return low - 1

            

