class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        stk_idx = -1 #Marks the index of the topmost element on the stack
        for op_idx, op in enumerate(operations):
            if op == 'C':
                stk.pop()
                stk_idx -= 1
                continue
            else:
                if op == '+':
                    stk.append(stk[stk_idx] + stk[stk_idx-1])
                elif op == 'D':
                    stk.append(stk[stk_idx]*2)
                else:
                    op = int(op)
                    stk.append(op)

                stk_idx += 1
            
        
        print(stk)
        return sum(stk)