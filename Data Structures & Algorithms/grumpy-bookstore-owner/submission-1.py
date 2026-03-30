class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        numCustomers = len(customers)
        # Handle base-case where number of customers is < minutes here
        if numCustomers <= minutes:
            return sum(customers)

        curGain = 0
        for i in range(minutes):
            curGain += grumpy[i] * customers[i]

        maxGain = curGain
        for l in range(1, numCustomers - minutes + 1):
            r = l + minutes - 1
            curGain += customers[r] * grumpy[r]
            curGain -= customers[l-1] * grumpy[l-1]
            if curGain > maxGain:
                maxGain = curGain
        
        alreadySatisfied = sum(customers[i] for i in range(numCustomers) if not grumpy[i])
        return alreadySatisfied + maxGain



