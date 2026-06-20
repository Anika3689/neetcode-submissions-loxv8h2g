class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
            
        q = deque()
        q.append([0, 0, 0, 0])
        visited = set()
        turns = 0
        while q:
            level_size = len(q)
            for _ in range(level_size):
                curState = q.popleft()
                curStateStr = ''.join(map(str, curState))
                if curStateStr == target:
                    return turns
                
                for i in range(4):
                    curState[i] = (curState[i] + 1) % 10
                    curStateStr = ''.join(map(str, curState))
                    if curStateStr not in deadends and curStateStr not in visited:
                        q.append(curState.copy())
                        visited.add(curStateStr)

                    curState[i] = (curState[i] - 2) % 10
                    curStateStr = ''.join(map(str, curState))
                    if curStateStr not in deadends and curStateStr not in visited:
                        q.append(curState.copy())
                        visited.add(curStateStr)

                    curState[i] = (curState[i] + 1) % 10
            
            #print(q, level_size)
            turns += 1
        
        return -1
