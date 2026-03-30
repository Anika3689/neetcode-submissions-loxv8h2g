class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort cars by increasing position
        cars = sorted(zip(position, speed), reverse=True)
        timesToFinish = [(target - pos) / speed for pos, speed in cars]
        numFleets = 0
        maxTimeToFinish = 0

        for time in timesToFinish:
            if time > maxTimeToFinish:
                maxTimeToFinish = time
                numFleets += 1
        
        return numFleets