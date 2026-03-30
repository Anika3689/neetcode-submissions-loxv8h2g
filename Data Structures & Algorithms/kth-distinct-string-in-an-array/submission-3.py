class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        
        for string in arr:
            if counts[string] == 1 and k == 1:
                return string
            if counts[string] == 1:
                k -= 1
        
        return ""
            
        
