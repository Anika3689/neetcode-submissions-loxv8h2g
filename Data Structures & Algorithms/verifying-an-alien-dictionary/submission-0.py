class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # stores the order of letters in the alien alphabet
        letterPositions = {order[i] : i for i in range(len(order))}
        def compare(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
                if letterPositions[word1[i]] > letterPositions[word2[i]]:
                    return False
                if letterPositions[word1[i]] < letterPositions[word2[i]]:
                    return True
                i += 1
                
            # if right word is a prefix of left word
            if i >= len(word2) and i < len(word1):
                return False
            return True
                
        for i in range(len(words)-1):
            if not compare(words[i], words[i+1]):
                return False
        
        return True