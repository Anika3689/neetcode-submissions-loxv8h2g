class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort trips by start distance
        trips.sort(key = lambda trip : trip[1])
        totalPassengers = 0
        # stores (arrival distance, num passengers)
        activeTrips = []

        for trip in trips:
            curTripPassengers, curStart, curFinish = trip
            # handle trips that have already arrived 
            while activeTrips and activeTrips[0][0] <= curStart:
                arrivedTrip = heapq.heappop(activeTrips)
                totalPassengers -= arrivedTrip[1]
            
            if totalPassengers + curTripPassengers > capacity:
                return False

            totalPassengers += curTripPassengers
            heapq.heappush(activeTrips, (curFinish, curTripPassengers)) 

        return True