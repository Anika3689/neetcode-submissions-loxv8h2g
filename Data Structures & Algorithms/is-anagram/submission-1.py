class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_counts = defaultdict(int)
        for ch in s:
            s_counts[ch] += 1
        
        for ch in t:
            if s_counts.get(ch, -1) > 0:
                s_counts[ch] -= 1
                if s_counts[ch] == 0:
                    s_counts.pop(ch)
            else:
                return False
        
        return len(s_counts) == 0
