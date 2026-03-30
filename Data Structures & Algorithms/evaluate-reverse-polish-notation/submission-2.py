class Solution:
    def do_op(op, a, b):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = ['+', '-', '*', '/']
        for token in tokens:
            if token in ops:
                b, a = stk.pop(), stk.pop()
                res = Solution.do_op(token, a, b)
                stk.append(res)
            else:
                stk.append(int(token))
        
        return stk[-1]
