class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if (target + total) % 2 != 0:
            return 0
        if abs(target) > sum(nums): 
            return 0

        P = (target + total) //2
        n = len(nums)

        dp = [[0] * (P+1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            num = nums[i-1]
            for s in range(0, P + 1):
                dp[i][s] = dp[i-1][s]

                if s >= num:
                    dp[i][s] += dp[i-1][s - num]

        return dp[n][P]
