class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreqs = Counter(tasks)
        maxHeap = [-taskFreqs[task] for task in taskFreqs]
        heapq.heapify(maxHeap)

        # (time t when available, remaining count)
        cooldown = deque()
        time = 0

        while maxHeap or cooldown:
            time += 1
            if cooldown and cooldown[0][0] == time:
                _, count = cooldown.popleft()
                heapq.heappush(maxHeap, count)
            
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count != 0:
                    cooldown.append((time + n + 1, count))
                
        
        return time
            

            

