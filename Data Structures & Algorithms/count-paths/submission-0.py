class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n: 
            return 0
        
        dp = [[1] * n for i in range(m)]

        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[m-1][n-1]

