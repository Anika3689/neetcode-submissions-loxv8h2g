class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]
        decStk = [0]

        for day in range(1, len(temperatures)):
            curTemp = temperatures[day]
            while decStk and curTemp > temperatures[decStk[-1]]:
                prevDay = decStk.pop()
                result[prevDay] = day - prevDay

            decStk.append(day)
        
        return result
            


            
            