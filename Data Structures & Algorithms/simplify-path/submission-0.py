class Solution:
    def simplifyPath(self, path: str) -> str:
        path_parts = path.split('/')
        result = []
        for path in path_parts:
            if path == '' or path == '.':
                continue
            elif path == '..':
                if len(result) > 0:
                    result.pop()
            else:
                result.append(path)

        if len(result) == 0:
            result = '/'
        else:
            result = '/' + '/'.join(result)
        return result

