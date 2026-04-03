class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        
        def helper(letterCombo: list, i: int):
            if i == len(digits):
                if letterCombo:
                    allPossible.append(''.join(letterCombo))
                return
            
            for letter in letterMappings[digits[i]]:
                letterCombo.append(letter)
                helper(letterCombo, i + 1)
                letterCombo.pop()
        
        allPossible = []
        helper([], 0)
        return allPossible