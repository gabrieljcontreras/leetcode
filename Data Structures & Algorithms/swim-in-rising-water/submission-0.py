import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        min_heap = [(grid[0][0], 0, 0)]
        visited = set()

        while min_heap: 
            max_val, r, c = heapq.heappop(min_heap)

            if r == rows - 1 and c == cols -1: 
                return max_val
            
            if (r,c) in visited: 
                continue 
            visited.add((r,c))

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = dr + r, dc + c

                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    neighbor_time = max(max_val, grid[nr][nc])
                    heapq.heappush(min_heap, (neighbor_time, nr, nc))

        return 0

