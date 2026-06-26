class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: 
            return []
        
        rows = len(heights)
        cols = len(heights[0])

        pacific_reachable = set()
        atlantic_reachable = set()



        def dfs(r,c, reachable_set, prev_height): 
            if (r < 0 or c < 0 or r >= rows or c >= cols 
                or (r,c) in reachable_set or 
                heights[r][c] < prev_height) : 
                return 

            reachable_set.add((r,c))

            dfs(r+1,c,reachable_set, heights[r][c])
            dfs(r-1,c,reachable_set, heights[r][c])
            dfs(r,c+1,reachable_set, heights[r][c])
            dfs(r,c-1,reachable_set, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific_reachable, heights[0][c])
            dfs(rows-1, c, atlantic_reachable, heights[rows-1][c])
        for r in range(rows): 
            dfs(r,0,pacific_reachable, heights[r][0])
            dfs(r,cols-1,atlantic_reachable, heights[r][cols-1])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific_reachable and (r,c) in atlantic_reachable: 
                    res.append([r,c])
        return res
