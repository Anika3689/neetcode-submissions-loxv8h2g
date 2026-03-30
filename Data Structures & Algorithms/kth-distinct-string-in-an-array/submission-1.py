class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        unique_strs = {string for string in counts
                                if counts[string] == 1}
        
        print(unique_strs)
        for string in arr:
            if string in unique_strs and k == 1:
                return string
            if string in unique_strs:
                k -= 1
        
        return ""
            

        
