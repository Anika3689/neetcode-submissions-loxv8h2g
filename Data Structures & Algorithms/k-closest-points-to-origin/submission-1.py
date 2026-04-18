class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        tagged_points = [(point[0] **2 + point[1] **2, point) for point in points]
        heapq.heapify(tagged_points)
        closest_points = []
        while len(closest_points) < k:
            closest_points.append(heapq.heappop(tagged_points)[1])
        
        return closest_points