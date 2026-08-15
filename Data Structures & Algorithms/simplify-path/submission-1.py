class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for part in path:
            if part == '' or part == '.':
                continue
            if part == '..': 
                if stack:
                    stack.pop()
                continue
            
            stack.append(part)
        
        return '/' + '/'.join(stack)
