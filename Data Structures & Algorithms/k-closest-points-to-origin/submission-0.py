import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points: 
            x,y = p
            dist = x**2 + y**2
            heapq.heappush(heap,(-dist,p))

            if len(heap) > k: 
                heapq.heappop(heap)

        return [p for dist, p in heap]