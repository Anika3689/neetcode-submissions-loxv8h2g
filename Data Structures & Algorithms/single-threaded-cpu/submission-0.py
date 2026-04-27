class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # (index, available_time, proc_time)
        tasks = [(i, tasks[i][0], tasks[i][1]) for i in range(len(tasks))]
        tasks.sort(key = lambda task : task[1])
        time = tasks[0][1]
        # (processing_time, index)
        availableTasks = [] 
        # index of earliest currently unavailable task, in sorted tasks
        i = 0  

        ordering = []
        while i < len(tasks) or availableTasks:
            # Each iteration represents a time = t at the end of a task
            while i < len(tasks) and tasks[i][1] <= time:
                heapq.heappush(availableTasks, (tasks[i][2], tasks[i][0]))
                i += 1
            
            if availableTasks:
                procTime, nextTaskIndex = heapq.heappop(availableTasks)
                ordering.append(nextTaskIndex)
                time += procTime
            else:
                time = tasks[i][1]
            
        return ordering
        
        
