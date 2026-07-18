class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(rem):
            if rem == 0: 
                return 0 
            if rem < 0 : 
                return float('inf')
            if rem in memo: 
                return memo[rem]
            
            min_coins = float('inf')

            for coin in coins: 
                res = dfs(rem - coin)

                if res != float('inf'):
                    min_coins = min(min_coins, 1 + res)

            memo[rem] = min_coins
            return min_coins 
        result = dfs(amount)

        return result if result != float('inf') else -1
        