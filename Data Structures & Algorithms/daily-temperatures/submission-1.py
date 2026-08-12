class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decStack = []
        res = [0] * len(temperatures)

        for i, curTemp in enumerate(temperatures):
            while decStack and curTemp > decStack[-1][0]:
                prevTemp, j = decStack.pop()
                res[j] = i - j
            
            decStack.append((curTemp, i))
        
        return res
