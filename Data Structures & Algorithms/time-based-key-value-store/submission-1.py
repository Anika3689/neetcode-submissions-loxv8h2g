class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or len(self.map[key]) == 0:
            return ""

        keyList = self.map[key]
        low = 0
        high = len(keyList)

        while low < high:
            mid = (low + high) // 2
            t, val = keyList[mid]
            if t <= timestamp:
                low = mid + 1
            else:
                high = mid

        if low > 0:
            return keyList[low-1][1]
        return ""
