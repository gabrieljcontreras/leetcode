class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0 

        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        
        def dfs(r, c): 
            if memo[r][c] != 0: 
                return memo[r][c]
            
            max_path = 1

            directions = [(-1,0),(1,0), (0,1), (0,-1)]
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(nr,nc))

            memo[r][c] = max_path
            return memo[r][c]
        longest_path = 0
        for r in range(rows):
            for c in range(cols):
                longest_path = max(longest_path, dfs(r,c))

        return longest_path