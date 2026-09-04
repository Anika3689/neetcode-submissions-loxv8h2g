class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []

        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
            
        vals = self.map[key]
        if vals[0][1] > timestamp:
            return ""

        largestTsIndex = 0
        l = 0
        r = len(vals) - 1

        while l <= r:
            mid = (l + r) // 2
            prevVal, prevTs = vals[mid]
            if prevTs == timestamp:
                return prevVal

            elif prevTs < timestamp:
                largestTsIndex = mid
                l = mid + 1
            else:
                r = mid - 1

        return vals[largestTsIndex][0]




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)