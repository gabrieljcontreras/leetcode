class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            temp_price = list(prices)

            for u, v, price in flights: 
                if prices[u] == float('inf'):
                    continue 
                if prices[u] + price < temp_price[v]:
                    temp_price[v] = prices[u] + price
            
            prices = temp_price
        
        return prices[dst] if prices[dst] != float('inf') else -1

        
