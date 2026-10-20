class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stk = []
        answers = [0] * len(temperatures)

        for j in range(len(temperatures)):
            while stk and (prevTemp := stk[-1][1]) < temperatures[j]:
                i, _ = stk.pop()
                answers[i] = j - i

            stk.append((j, temperatures[j]))
        
        return answers