class Solution:
    def findPeak(self, mountain, n):
        left = 0
        right = n-1
        while left < right:
            mid = (left + right) // 2
            midElem = mountain.get(mid)
            lneighbor = mountain.get(mid-1)
            rneighbor = mountain.get(mid+1)
            
            if lneighbor < midElem and midElem > rneighbor:
                return mid
            elif midElem < rneighbor:
                left = mid + 1
            else:
                right = mid

        if left == right:
            return left
        return -1

    def findInSorted(self, arr, target, left, right, reverse=False):
        while left <= right:
            mid = (left+right)//2
            if arr.get(mid) == target:
                return mid
            if target > arr.get(mid):
                if reverse:
                    right = mid - 1
                else:
                    left = mid + 1  
            else:
                if reverse:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        peakIdx = self.findPeak(mountainArr, n)
        peakElem = mountainArr.get(peakIdx)
        if peakElem == target:
            return peakIdx

        if mountainArr.get(0) <= target < peakElem:
            found = self.findInSorted(mountainArr, target, 0, peakIdx-1)
            if found != -1:
                return found
        if target < peakElem and target >= mountainArr.get(n-1):
            return self.findInSorted(mountainArr, target, peakIdx+1, n-1, True)
        
        return -1
        





