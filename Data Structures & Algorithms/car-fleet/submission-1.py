class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for pos, speed in zip(position, speed):
            remainingTime = (target - pos) / speed
            cars.append((pos,remainingTime))
        
        cars.sort(reverse=True)
        numFleets = 0
        fleetTime = 0
        for _, time in cars:
            if time > fleetTime:
                numFleets += 1
                fleetTime = time
            
        
        return numFleets