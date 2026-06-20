class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island_counter = 1
        
        if not grid: 
            return 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]):
                return 0
            
            if grid[r][c] != 1:
                return 0
            grid[r][c] = island_counter

            area = 1 + dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)

            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island_counter += 1
                    max_area = max(max_area, dfs(r,c))
        return max_area