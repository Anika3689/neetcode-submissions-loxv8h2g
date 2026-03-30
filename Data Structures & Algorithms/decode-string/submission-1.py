class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for ch in s:
            if ch != ']':
                stk.append(ch)
                continue

            sub_encoded = []
            # Get the susbtring between these pair of brackets
            while stk and stk[-1] != '[':
                sub_encoded.append(stk.pop())
            stk.pop()
            repeat_times = i = 0
            while stk and stk[-1].isdigit():
                repeat_times += int(stk.pop()) * (10 ** i)
                i += 1
        
            sub_encoded.reverse()
            stk += sub_encoded * repeat_times
        
        return ''.join(stk)
            
                    
            