class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        padded_nums = [1] + nums + [1]
        n = len(padded_nums)
        memo = {}

        def dfs(l,r):
            if l + 1 == r: 
                return 0
            if (l, r) in memo:
                return memo[(l,r)]
            coins = 0

            for k in range(l + 1, r):
                coins_from = padded_nums[l] * padded_nums[k] * padded_nums[r]
                total = dfs(k, r) + dfs(l, k) + coins_from
                coins = max(total, coins)

            memo[(l,r)] = coins
            return coins
        return dfs(0, n-1)



