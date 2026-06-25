from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        min_passed = 0
        fresh_oranges = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    fresh_oranges += 1
                elif grid[r][c] == 2: 
                    queue.append((r, c))

        while queue and fresh_oranges > 0: 
            rotted_this_min = False

            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: 
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        queue.append((nr, nc))
                        rotted_this_min = True

            if rotted_this_min:
                min_passed += 1

        if fresh_oranges > 0:
            return -1

        return min_passed