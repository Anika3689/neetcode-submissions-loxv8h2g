class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # original index, enqueue_time, proc_time
        tasks = [(i, tasks[i][0], tasks[i][1]) for i in range(len(tasks))]
        tasks.sort(key = lambda task : task[1])
        availableTasks = []
        curTime = tasks[0][1]
        i = 0

        taskOrdering = []
        while i < len(tasks) or availableTasks:
            # add newly available tasks
            while i < len(tasks) and tasks[i][1] <= curTime:
                heapq.heappush(availableTasks, (tasks[i][2], tasks[i][0]))
                i += 1
            
            if availableTasks:
                procTime, taskIndex = heapq.heappop(availableTasks)
                taskOrdering.append(taskIndex)
                curTime += procTime
            else:
                curTime = tasks[i][1]
            
        return taskOrdering
        
