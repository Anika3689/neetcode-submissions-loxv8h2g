class Solution:
    def is_palindrome(self, string, l, r):
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:

        def generatePartitions(l):
            allPartitions = []
            for i in range(l, len(s)):
                if not self.is_palindrome(s, l, i):
                    continue

                partitions = generatePartitions(i + 1)
                if not partitions:
                    allPartitions.append([s[l:i + 1]])
                for partition in partitions:
                    allPartitions.append([s[l:i + 1]] + partition)
            
            return allPartitions
        
        allPartitions = generatePartitions(0)
        return allPartitions
        


