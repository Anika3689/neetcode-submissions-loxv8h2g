class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreqs = Counter(tasks)
        prevN = deque(maxlen=n)
        minIntervals = 0

        while any([taskFreqs[task] for task in taskFreqs]):
            highestFreq = 0
            mostFreqTask = None
            for task in taskFreqs:
                if task in prevN:
                    continue
                if taskFreqs[task] > highestFreq:
                    highestFreq = taskFreqs[task]
                    mostFreqTask = task
            
            minIntervals += 1
            if mostFreqTask:
                taskFreqs[mostFreqTask] -= 1
                prevN.append(mostFreqTask)
            else:
                prevN.append('-')
        
        return minIntervals