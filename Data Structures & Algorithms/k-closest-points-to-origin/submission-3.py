class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        tagged_points = [(-(point[0] **2 + point[1] **2), point) for point in points]
        heap = []
        for point in tagged_points:
            if len(heap) < k:
                heapq.heappush(heap, point)
                continue
            
            if point[0] > heap[0][0]:
                heapq.heapreplace(heap, point)
        
        res = [point for _, point in heap]
        return res
            
