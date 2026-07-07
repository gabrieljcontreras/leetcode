import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points: 
            return 0
        
        n = len(points)
        visited = set()
        min_heap = [(0,0)]
        total_cost = 0

        while len(visited) < n: 
            cost, curr_point = heapq.heappop(min_heap)

            if curr_point in visited: 
                continue 
            
            visited.add(curr_point)
            total_cost += cost

            x1,y1 = points[curr_point]

            for next_point in range(n):
                if next_point not in visited: 
                    x2, y2 = points[next_point]
                    distance = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(min_heap, (distance, next_point))
        return total_cost

            